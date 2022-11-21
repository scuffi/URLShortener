import redis

from config import RedisConfig

class RedisClient:
    """
    This class acts as a utility class to ease getting and setting of shortened url's into the redis database.
    
    All functions are classmethods, so you do not need to instantiate this class to access them
    """
    
    # Define our client outside of the methods so we only need to create a client once.
    client = redis.Redis(host=RedisConfig.HOST, port=RedisConfig.PORT, db=0, password=RedisConfig.PASSWORD)
    
    @classmethod
    def url_exists(cls, url: str):
        pass
    
    @classmethod
    def add_url(cls, shortened_key: str, url: str,):
        pass
    
    @classmethod
    def get_url(cls, shortened_key: str):
        pass