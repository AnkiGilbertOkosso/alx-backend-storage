#!/usr/bin/env python3
'''Task 12.
This module provides functionality to analyze Nginx request logs stored
in a MongoDB collection.
'''

from pymongo import MongoClient

def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs.
    Args:
        nginx_collection: A PyMongo collection object representing the
        Nginx logs collection in MongoDB.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))

def run():
    '''Provides some statistics about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)

if __name__ == '__main__':
    run()