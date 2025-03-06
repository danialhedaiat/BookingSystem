from motor.motor_asyncio import AsyncIOMotorClient
import redis

from config import MONGO_HOST,REDIS_HOST


class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            cls._instance.mongo_client = AsyncIOMotorClient(MONGO_HOST)
            cls._instance.db = cls._instance.mongo_client['booking_system']
            cls._instance.log_collection = cls._instance.db['log']
            cls._instance.redis = None
        return cls._instance

    def __init__(self):
        if self.redis is None:
            self.redis = redis.asyncio.from_url(REDIS_HOST, decode_responses=True)


