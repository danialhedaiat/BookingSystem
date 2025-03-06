from datetime import datetime

from pydantic import BaseModel


class BookingRequest(BaseModel):
    seat_id: str
    user_id: str
    name: str
    data: datetime