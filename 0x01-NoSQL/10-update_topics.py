#!/usr/bin/env python3
"""
Change all the school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    function that updates all topics of a school document based on name
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
