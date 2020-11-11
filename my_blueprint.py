import redis

from flask import Blueprint

class YcSearch(Blueprint):
    def __init__(self, name, import_name, static_folder=None, static_url_path=None, template_folder=None,
                 url_prefix=None, subdomain=None, url_defaults=None, root_path=None):
        super().__init__(name, import_name, static_folder, static_url_path, template_folder, url_prefix, subdomain,
                         url_defaults, root_path)

app = YcSearch('ycSearch', __name__)
r = redis.Redis(host='localhost', port=6379)

@app.route('/modules')
def get_modules():
    return r.get('modules-data').decode('utf-8')

@app.route('/vendors')
def get_vendors():
    return r.get('vendors-data').decode('utf-8')
