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

