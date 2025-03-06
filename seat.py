from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from DB import DB
from dtos import Seat, DeleteSeat, UpdateSeat

router = APIRouter()


@router.get("/all")
async def seats():
    db = DB()
    collection = db.db["seats"]
    cursor = collection.find({},
                             {"_id": 0})
    data = await cursor.to_list()
    return JSONResponse(data)


@router.post("/create")
async def create_seat(request: Seat):
    db = DB()
    mongo_seat = await db.booking_collection.find_one({"seat_id": request.seat_id})
    print(mongo_seat)
    if mongo_seat:
        raise HTTPException(status_code=409, detail="id was used before")

    db.booking_collection.insert_one({
        "seat_id": request.seat_id,
        "user_id": request.user_id,
        "status": request.status,
        "name": "",
        "data": None

    })

    return {"message": "success", "seat_id": request.seat_id}


@router.post("/update")
async def update_seat(request: UpdateSeat):
    db = DB()
    mongo_seat = await db.booking_collection.find_one({"seat_id": request.seat_id})
    if not mongo_seat:
        return HTTPException(status_code=406, detail="id was not fund")

    db.booking_collection.update_one({"seat_id": request.seat_id}, {
        "$set":
            {
                "user_id": request.user_id,
            }
    })

    return {"message": "success", "seat_id": request.seat_id}


@router.post("/delete")
async def delete_seat(request: DeleteSeat):
    db = DB()
    mongo_seat = await db.booking_collection.find_one({"seat_id": request.seat_id})
    if not mongo_seat:
        raise HTTPException(status_code=406, detail="id was not fund")

    db.booking_collection.delete_one({"seat_id": request.seat_id})

    return {"message": "success", "seat_id": request.seat_id}
