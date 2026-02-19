from main import data


for doc in data:
    if doc["weapons_count"] > 0 or doc["distance_from_fence_m"] <= 50 or doc["people_count"] >= 8 or doc["vehicle_type"] == "truck" or (doc["distance_from_fence_m"] <= 150 and doc["people_count"] >= 4) or (doc["vehicle_type"] == "jeep" and doc["people_count"] >= 3):
        doc["priority"] == "URGENT"
    else:
         doc["priority"] == "NORMAL"
         