from mongo_connection import collection



def analytics_alerts_by_border_and_priority_mongo():
    
    pipeline = [
        {
            "$group": {
                "_id": ["$border","$priority"],
                "count": {"$sum":1}
            }
        },{
            "$project": {
                "_id": 0,
                "area_and_risk": "$_id",
                "count": 1

            }}

    ]

    return list(collection.aggregate(pipeline))





def analytics_top_urgent_zones_mongo():
    pipeline = [
        {
            "$group": {
                "_id": "$border",
                "count": {"$sum":1}
            }
        },{
            "$project": {
                "_id": 0,
                "area_and_risk": "$_id",
                "count": 1

            }}, {
                    "$sort": {"count": -1}
                 },{"$limit": 5}
    ]

    return list(collection.aggregate(pipeline))



def analytics_distance_distribution_mongo():
    pipeline = [
        {
            "$group": {
                "_id": "$distance_from_fence_m",
                "count": {"$sum":1}
            }
        },
        {
            "$project": {
                "_id": 0,
                "distance_from_fence_m": "$_id",
                "count": 1
            }},{"$sort": {"total": -1}
}
    ]

    return list(collection.aggregate(pipeline))





def analytics_low_visibility_high_activity_mongo():
    pass

def analytics_hot_zones_mongo():
    pass