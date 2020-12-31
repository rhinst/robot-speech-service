import os
from itertools import cycle
from time import sleep
from typing import Dict
import json

from redis import Redis
from redis.client import PubSub

from speech.config import load_config
from speech import talker
from speech.logging import logger, initialize_logger


def main():
    environment: str = os.getenv("ENVIRONMENT", "dev")
    config: Dict = load_config(environment)
    initialize_logger(config['logging']['level'], config['logging']['filename'])
    redis_host = config['redis']['host']
    redis_port = config['redis']['port']
    logger.debug(f"Connecting to redis at {redis_host}:{redis_port}")
    redis_client: Redis = Redis(
        host=redis_host, port=redis_port
    )
    pubsub: PubSub = redis_client.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("subsystem.speech.command")
    while cycle([True]):
        try:
            # see if there is a command for me to execute
            if redis_message := pubsub.get_message():
                message = redis_message
                talker.say(message["data"])
            sleep(0.25)
        finally:
            pubsub.close()
            redis_client.close()


if __name__ == '__main__':
    main()
