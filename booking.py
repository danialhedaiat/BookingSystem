
from fastapi import APIRouter, HTTPException
from DB import DB
from dtos import BookingRequest
from log import log_action

router = APIRouter()

@router.post("/bookSeat")
async def bookSeat(request: BookingRequest):
    redis = DB().redis
    seat_status = await redis.get(f"seat:{request.seat_id}")

    if seat_status and seat_status != "available":
        raise HTTPException(status_code = 400, detail="Seat is not available")

    await redis.set(f"seat:{request.seat_id}", "booked")

    await log_action("booking", request.user_id, request.seat_id, details={"customer_name": request.name})

    return {"message": "success", "seat_id": request.seat_id}