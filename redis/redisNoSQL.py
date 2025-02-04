import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# création
r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')

print(r.get('user:1:name'))

r.set('user:1:name', 'jason')

print(r.get('user:1:name'))

r.delete('user:1:name', 'jason')

print(r.get('user:1:name'))