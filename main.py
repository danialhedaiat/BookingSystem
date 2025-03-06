import asyncio

import uvicorn
from fastapi import FastAPI

import booking
from DB import DB


app = FastAPI()
app.include_router(booking.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Ticket Booking System"}


if __name__ == "__main__":
    db = DB()
    asyncio.run(db.init_redis())
    uvicorn.run(app, host="0.0.0.0", port=8000)
