#!/usr/bin/env python3
"""
return all students by average score
"""


def top_students(mongo_collection):
    """ function that returns all students by average score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
