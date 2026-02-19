from fastapi import FastAPI
from mongo_connection import collection
from dal import *
from testing_in_redis import *
import json


app =  FastAPI()



@app.get("/analytics/alerts-by-border-and-priority")
def analytics_alerts_by_border_and_priority():
        memory = q_1() 
        if memory == False:
            return analytics_alerts_by_border_and_priority_mongo()
        else:
             return json.dumps(memory)




@app.get("/analytics/top-urgent-zones")
def analytics_top_urgent_zones():
        memory = q_2() 
        if memory == False:
            return analytics_top_urgent_zones_mongo()
        else:
             return json.dumps(memory)





@app.get("/analytics/distance-distribution")
def analytics_distance_distribution():
    memory = q_3() 
    if memory == False:
        return analytics_distance_distribution_mongo()
    else:
        return json.dumps(memory)






@app.get("/analytics/low-visibility-high-activity")
def analytics_low_visibility_high_activity():
    memory = q_4() 
    if memory == False:
        return analytics_low_visibility_high_activity_mongo()
    else:
        return json.dumps(memory)


@app.get("/analytics/hot-zones")
def analytics_hot_zones():
    pass



