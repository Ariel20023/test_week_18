import os
from pymongo import MongoClient


client = MongoClient("mongodb://mongodb:27017")

db = client.test_18

collection = db.suspects

print("Mongo connected")

