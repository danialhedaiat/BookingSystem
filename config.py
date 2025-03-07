import os


MONGO_HOST = os.getenv("MONGO_HOST", "mongodb://admin:1234@localhost/")
REDIS_HOST = os.getenv("REDIS_HOST", 'redis://localhost:6379')
RESERVATION_TIMEOUT = 300