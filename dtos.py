from datetime import datetime

from pydantic import BaseModel


class BookingRequest(BaseModel):
    seat_id: int
    user_id: int
    name: str
    data: datetime


class ReservationRequest(BaseModel):
    seat_id: int
    user_id: int
    name: str
    data: datetime


class CancelRequest(BaseModel):
    seat_id: int
    user_id: int
    name: str


class Seat(BaseModel):
    seat_id: int
    user_id: int = None
    status: str = "available"


class UpdateSeat(BaseModel):
    seat_id: int
    user_id: int = None


class DeleteSeat(BaseModel):
    seat_id: int