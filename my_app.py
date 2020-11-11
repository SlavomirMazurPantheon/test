from flask import Flask
import redis
from my_blueprint import app as search_app

app = Flask(__name__)
app.register_blueprint(search_app)

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

@app.route('/')
def hello_world():
    return 'Hello, World!'
