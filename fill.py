import json
import os
from collections import OrderedDict

import redis

redis_cache = redis.Redis(host='localhost', port=6379)

redis_cache.set('a', 'a')
redis_cache.set('b', 'b')
redis_cache.set('c', 'c')

def load_catalog_data():
    resources_path = '{}/resources/'.format(os.path.dirname(os.path.abspath(__file__)))
    try:
        with open('{}2020-10-21_00:00:00-UTC.json'.format(resources_path), 'r') as file_load:
            catalog_data = json.load(file_load, object_pairs_hook=OrderedDict)
    except:
        print('Failed to load data from .json file')

    catalog = catalog_data.get('yang-catalog:catalog')
    modules = catalog['modules']['module']
    vendors = catalog['vendors']['vendor']

    for module in modules:
        if module['name'] == 'yang-catalog' and module['revision'] == '2018-04-03':
            redis_cache.set('yang-catalog@2018-04-03/ietf', json.dumps(module))
            break

    catalog_data_json = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(json.dumps(catalog_data))['yang-catalog:catalog']
    modules = catalog_data_json['modules']
    if catalog_data_json.get('vendors'):
        vendors = catalog_data_json['vendors']
    else:
        vendors = {}
    redis_cache.set('modules-data', json.dumps(modules))
    redis_cache.set('vendors-data', json.dumps(vendors))
    redis_cache.set('all-catalog-data', json.dumps(catalog_data))

load_catalog_data()
