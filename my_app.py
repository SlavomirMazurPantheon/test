from flask import Flask
import redis
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379)
r.set('foo1', 'bar')

@app.route('/test2')
def test2():
    return r.get('a').decode('utf-8')

@app.route('/test3')
def test3():
    return r.get('b').decode('utf-8')

@app.route('/test4')
def test4():
    return r.get('c').decode('utf-8')

@app.route('/test')
def test():
    return r.get('foo1').decode('utf-8')

@app.route('/modules')
def test_modules():
    return r.get('modules-data').decode('utf-8')

@app.route('/vendors')
def test_vendors():
    return r.get('vendors-data').decode('utf-8')

@app.route('/')
def hello_world():
    return 'Hello, World!'
