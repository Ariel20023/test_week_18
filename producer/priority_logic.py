from main import data
from redis_connection import urgent_queue , normal_queue
import json



for doc in data:
    if doc["weapons_count"] > 0 or doc["distance_from_fence_m"] <= 50 or doc["people_count"] >= 8 or doc["vehicle_type"] == "truck" or (doc["distance_from_fence_m"] <= 150 and doc["people_count"] >= 4) or (doc["vehicle_type"] == "jeep" and doc["people_count"] >= 3):
        doc["priority"] == "URGENT"
        urgent_queue.set("doc", json.dumps(doc))

    else:
        doc["priority"] == "NORMAL"
        normal_queue.set("doc", json.dumps(doc))
