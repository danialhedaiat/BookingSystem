from datetime import datetime
from DB import DB


async def log_action(action_type, user_id, seat_id, details=""):
    log_entry = {
        "action_type": action_type,
        "user_id": user_id,
        "seat_id": seat_id,
        "details": details,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    db = DB()
    await db.log_collection.insert_one(log_entry)