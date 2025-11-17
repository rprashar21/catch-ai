import redis

redis = redis.Redis(host='localhost', port=6379, db=0)

# check connection
try:
    if redis.ping():
        print("redis is connected at ")
except Exception:
    print("No connection for redis")

redis.set("name","rohit")