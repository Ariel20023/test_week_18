from redis_connection import r
import json
from dal import *

def q_1():
    exists = r.answer.exists("analytics_alerts_by_border_and_priority")
    if exists == 1:
        answer = r.answer.get("analytics_alerts_by_border_and_priority")
        answer_list = json.loads(answer)
        return answer_list
    else:
        answer_from_mongo = analytics_alerts_by_border_and_priority_mongo()
        r.answer.set("analytics_alerts_by_border_and_priority" ,json.dumps(answer_from_mongo))
        return False





def q_2():
    exists = r.answer.exists("analytics_top_urgent_zones_mongo")
    if exists == 1:
        answer = r.answer.get("analytics_top_urgent_zones_mongo")
        answer_list = json.loads(answer)
        return answer_list
    else:
        answer_from_mongo = analytics_top_urgent_zones_mongo()
        r.answer.set("analytics_top_urgent_zones_mongo",json.dumps(answer_from_mongo))
        return False



def q_3():
    exists = r.answer.exists("analytics_distance_distribution")
    if exists == 1:
        answer = r.answer.get("analytics_top_urgent_zones_mongo")
        answer_list = json.loads(answer)
        return answer_list
    else:
        answer_from_mongo = analytics_distance_distribution_mongo()
        r.answer.set("analytics_distance_distribution",json.dumps(answer_from_mongo))
        return False


def q_4():
    pass



def q_5():
    pass

