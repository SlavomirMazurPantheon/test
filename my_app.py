from flask import Flask
import redis
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379)
r.set('foo1', 'bar')

@app.route('/test')
def test():
    return r.get('foo1').decode('utf-8')

@app.route('/')
def hello_world():
    return 'Hello, World!'

