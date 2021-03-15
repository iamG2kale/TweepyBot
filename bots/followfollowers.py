# This code allows bot to take the credentials from config file
# and follow the people automatically that are following you
# but aren't

import tweepy
from bots.config import create_api
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers...")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                logger.info(f"following user : {follower.name}")
                follower.follow();
            except tweepy.error.TweepError:
                pass

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("waiting")
        time.sleep(60)

if  __name__ == "__main__":
    main()
