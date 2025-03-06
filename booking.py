
from fastapi import APIRouter, HTTPException, BackgroundTasks
from DB import DB
from dtos import BookingRequest, ReservationRequest, CancelRequest
from log import log_action


router = APIRouter()


@router.post("/bookSeat")
async def book_seat(request: BookingRequest, background_tasks: BackgroundTasks):
    redis = DB().redis
    db = DB()
    reserve_seat = await redis.hgetall(f"seat:{request.seat_id}")
    mongo_seat = await db.booking_collection.find_one({"seat_id":request.seat_id})

    if not mongo_seat:
        raise HTTPException(status_code = 406, detail="Seat was not found.")

    if reserve_seat and reserve_seat["status"] == "reserved" and reserve_seat["user_id"] != request.user_id:
        raise HTTPException(status_code = 406, detail="Seat is reserved to someone else")

    if mongo_seat["status"] not in ["available", "reserved"]:
        raise HTTPException(status_code = 406, detail="Seat is not available")

    data = {
        'status': 'booked',
        'user_id': request.user_id
    }

    await db.booking_collection.update_one({"seat_id":request.seat_id},{"$set":data})
    await redis.delete(f"seat:{request.seat_id}")

    background_tasks.add_task(log_action, "booking", request.user_id, request.seat_id, details={"customer_name": request.name})

    return {"message": "success", "seat_id": request.seat_id}

@router.post("/reserveSeat")
async def reserve_seat(request: ReservationRequest, background_tasks: BackgroundTasks):
    db = DB()
    redis = db.redis
    reserve_seat = await redis.hgetall(f"reserve_seat:{request.seat_id}")
    mongo_seat = await db.booking_collection.find_one({"seat_id": request.seat_id})

    if not mongo_seat:
        raise HTTPException(status_code = 406, detail="Seat was not found.")

    if reserve_seat and reserve_seat["status"] != "available" or mongo_seat["status"] != "available":
        raise HTTPException(status_code = 406, detail="Seat is not available")

    data = {
        'id': request.seat_id,
        'status': 'reserved',
        'user_id': request.user_id
    }

    await redis.hset(f"reserve_seat:{request.seat_id}", mapping=data)
    await redis.expire(f"reserve_seat:{request.seat_id}", 300)
    background_tasks.add_task(log_action, "reserving", request.user_id, request.seat_id, details={"customer_name": request.name})

    return {"message": "success", "seat_id": request.seat_id}

@router.post("/cancelSeat")
async def cancel_seat(request: CancelRequest, background_tasks: BackgroundTasks):
    db = DB()
    redis = db.redis
    reserve_seat = await redis.hgetall(f"reserve_seat:{request.seat_id}")
    mongo_seat = await db.booking_collection.find_one({"seat_id": request.seat_id})

    if not mongo_seat:
        raise HTTPException(status_code = 406, detail="Seat was not found.")
    if (mongo_seat['status'] == "booked" and mongo_seat["user_id"] != request.user_id):
        raise HTTPException(status_code = 406, detail="Seat is booked for someone else")
    if mongo_seat["status"] != "booked":
        raise HTTPException(status_code=406, detail="Seat is not booked!")
    if reserve_seat and reserve_seat["status"] not in ["booked", "reserved"]:
        raise HTTPException(status_code = 406, detail="Seat is available")
    if reserve_seat and reserve_seat["user_id"] == request.user_id:
        raise HTTPException(status_code = 406, detail="Seat is reserved for someone else")


    data = {
        'status': 'available',
        'user_id': None
    }

    await db.booking_collection.update_one({"seat_id":request.seat_id},{"$set":data})
    background_tasks.add_task(log_action, "canceling", request.user_id, request.seat_id, {"customer_name": request.name})

    return {"message": "success", "seat_id": request.seat_id}