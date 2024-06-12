#!/usr/bin/env python3
'''provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


if __name__ == '__main__':
    '''database: logs
    collection - nginx
    Returns log stats'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    database = client.logs
    collection = database.nginx
    num_logs = collection.count_documents({})
    print(f'{num_logs} logs')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status_check = collection.count_documents(
            {'method': 'GET', 'path': '/status'}
            )
    print(f'{status_check} status check')

