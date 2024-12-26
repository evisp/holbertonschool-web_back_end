#!/usr/bin/env python3
"""A python module that manitpulates mongo DB"""


def schools_by_topic(mongo_collection, topic):
    """A function that returns the list of school having a specific topic"""

    all_schools = mongo_collection.find()
    topics_list = []
    for school in all_schools:
        if "topics" in school:
            if topic in school["topics"]:
                topics_list.append(school)
    return topics_list
