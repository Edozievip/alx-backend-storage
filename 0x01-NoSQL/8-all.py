#!/usr/bin/env python3
"""
List all documents using Python
"""
import pymongo


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
