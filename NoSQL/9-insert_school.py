#!/usr/bin/env python3
"""
Insert a new document into a Mongo collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in the collection based on kwargs

    Param:
        mongo_collection:
            The Mongo collection object
        kwargs:
            Key-value pairs representting the document fields

    Return: The ID of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
