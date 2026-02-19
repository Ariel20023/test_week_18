import os
from pymongo import MongoClient

client = MongoClient(
    host=os.getenv("MONGO_HOST"),
    port=int(os.getenv("MONGO_PORT", 27017)),
    username=os.getenv("MONGO_USER"),
    password=os.getenv("MONGO_PASSWORD"),
)

db = client[os.getenv("MONGO_DB", "test_18")]

collection = db.suspects

print("Mongo connected")
