#!/usr/bin/env python3
'''Task 14.
This module provides functionality to retrieve top students from a
MongoDB collection sorted by their average score.
'''

def top_students(mongo_collection):
    '''Retrieves top students from a collection sorted by average score.
    Args:
        mongo_collection: A PyMongo collection object containing student data.
    Returns:
        A cursor to the MongoDB documents representing top students sorted
        by average score.
    '''
    stud = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return stud
