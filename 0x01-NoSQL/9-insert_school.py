#!/usr/bin/env python3
"""
Insert a new document in the collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new documents into a collection based on kwargs
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
