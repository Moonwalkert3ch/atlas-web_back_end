#!/usr/bin/env python3
""" changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """mongo_collection - pymongo collection object
    name(str) - updated school name
    topics(str list) - list of topics
    Return - changed name"""
    view = {"name": name}
    updated = {"$set": {"topics": topics}}
    mongo_collection.update_many(view, updated)

