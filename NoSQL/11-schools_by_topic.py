#!/usr/bin/env python3
"""
Find schools by specific topic in Mongo
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find and return a list of schools having a specific topic

    Param:
        mongo_collection: The Mongo collection object
        topic: The topic to search for

    Return: Alist of schools with the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
