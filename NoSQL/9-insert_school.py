#!/usr/bin/env python3
""" inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """mongo_collection - pymongo collection object
    **kwargs - key args inputted
    Return - new id"""
    doc_id = mongo_collection.insert(**kwargs)
    return doc_id
