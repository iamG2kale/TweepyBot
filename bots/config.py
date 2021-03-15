import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    CONSUMER_KEY = os.getenv("tweepybotck")
    CONSUMER_SECRET = os.getenv("tweepybotcs")
    ACCESS_TOKEN = os.getenv("tweepybotat")
    ACCESS_SECRET = os.getenv("tweepybotas")

    print(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    if api:
        print("done")
    logger.info("API Created")
    return api
