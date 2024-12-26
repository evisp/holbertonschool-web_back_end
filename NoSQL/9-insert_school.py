#!/usr/bin/env python3
"""A python module that manitpulates mongo DB"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""

    the_object = mongo_collection.insert_one(kwargs)
    return the_object.inserted_id
