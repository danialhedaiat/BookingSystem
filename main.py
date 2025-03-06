import asyncio

import uvicorn
from fastapi import FastAPI

import booking
import mongo
import seat
from DB import DB


app = FastAPI()
app.include_router(booking.router)
app.include_router(mongo.router, prefix="/mongo")
app.include_router(seat.router, prefix="/seat")


@app.get("/")
async def root():
    return {"message": "Welcome to the Ticket Booking System"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
