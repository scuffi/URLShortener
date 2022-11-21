import os

class RedisConfig:
    """
    This class interfaces our redis environment variables for use in the redis client.
    
    Developer note: We use 'os.environ' here as this will throw an error on startup 
    if these environment variables don't exist, rather than just return 'None'
    """
    
    HOST = os.environ["REDIS_HOST"]
    PORT = os.environ["REDIS_PORT"]
    PASSWORD = os.environ["REDIS_PASSWORD"]
    