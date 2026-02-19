from redis_connection import urgent_queue , normal_queue
from datetime import datetime
import json
from mongo_connection import collection


def add_insertion_time(json_value):
    json_value["insertion_time"] = datetime.now()
    return json_value


def insert_to_mongo(ready_to_send):
    collection.insert_one(ready_to_send)
    print("inserted one document")



while True:
    if urgent_queue.get("doc"):
        value = urgent_queue.get("doc")
        json_value = json.loads(value)
        add_time = add_insertion_time(json_value)
        insert_to_mongo(add_time)
        continue
    else:
        value = normal_queue.get("doc")
        json_value = json.loads(value)
        add_time = add_insertion_time(json_value)
        insert_to_mongo(add_time)



