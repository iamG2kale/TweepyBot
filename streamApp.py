import json
from app import api
import json
import tweepy


class MyStreamClass(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        try:
            print(f"{tweet.user.name} : {tweet.text}")
        except BaseException as e:
            print("failed on date", str(e))

    def on_error(self, status):
        print("Error occurred")


streaming = MyStreamClass(api)
stream = tweepy.Stream(api.auth, streaming)
stream.filter(track=["aot"], languages=["en"])
