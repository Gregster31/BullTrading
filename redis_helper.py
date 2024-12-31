import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def save_to_redis(key, data, expiration=600):
    """Save data to Redis with a specified expiration time."""
    redis_client.set(key, json.dumps(data))
    redis_client.expire(key, expiration)

def get_from_redis(key):
    """Retrieve data from Redis."""
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None
