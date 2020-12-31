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
        host=redis_host, port=redis_port, db=0
    )
    pubsub: PubSub = redis_client.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("subsystem.speech.command")
    for redis_message in pubsub.listen():
        phrase = redis_message["data"]
        talker.say(phrase.decode('utf-8'))


if __name__ == '__main__':
    main()
