import redis

r = redis.Redis(host='localhost', port=6379)

r.set('a', 'a')
r.set('b', 'b')
r.set('c', 'c')
