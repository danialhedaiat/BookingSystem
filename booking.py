
from fastapi import APIRouter, HTTPException
from DB import DB
from dtos import BookingRequest
from log import log_action

router = APIRouter()

@router.post("/bookSeat")
async def bookSeat(request: BookingRequest):
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

    log_action("booking", request.user_id, request.seat_id, details={"customer_name": request.name})

    return {"message": "success", "seat_id": request.seat_id}