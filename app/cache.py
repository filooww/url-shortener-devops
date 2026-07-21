import redis

from app.config import settings

_client = None


def get_client():
    global _client
    if _client is None and settings.redis_url:
        _client = redis.from_url(settings.redis_url, decode_responses=True)
    return _client


def cache_get(code: str):
    client = get_client()
    if client is None:
        return None
    try:
        return client.get(f"link:{code}")
    except redis.RedisError:
        return None


def cache_set(code: str, target_url: str, ttl: int = 3600):
    client = get_client()
    if client is None:
        return
    try:
        client.set(f"link:{code}", target_url, ex=ttl)
    except redis.RedisError:
        pass
