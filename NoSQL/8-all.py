#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Return lists all documents in the collection MongoDB

    Parameter:
        mongo_collection: pymongo collection object

    Return: an empty list if no document in the collection
    """
    return list(mongo_collection.find())

