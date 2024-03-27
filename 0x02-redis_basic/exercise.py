import redis
import uuid
from typing import Union


class Cache:
    """
    A class to interact with Redis cache.

    Attributes:
    _redis (redis.Redis): An instance of Redis client.

    Methods:
    __init__: Initialize the Redis client and flush the database.
    store: Store data in Redis and return the generated key.
    """

    def __init__(self):
        """
        Initializes the Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.

        Args:
        data (Union[str, bytes, int, float]): The data to be stored in Redis.

        Returns:
        str: The generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
