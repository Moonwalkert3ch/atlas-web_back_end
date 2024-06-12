#!/usr/bin/env python3
""" returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """mongo_collection - pymongo collection object
    topic(str) - searched topic
    Return - specific topic"""
    document = mongo_collection.find({"topics": topic})
    return list(document)

