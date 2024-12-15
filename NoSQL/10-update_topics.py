#!/usr/bin/env python3
"""
Update the topics of a school documment in Mongo
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school doccument bases on the name

    Param:
        mongo_collection: The Mongo collection object
        name: The name of the school to update
        topics:The list of topics to set the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
