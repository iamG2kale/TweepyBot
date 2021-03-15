import tweepy
import random
import os

# first step is to set up authentication
CONSUMER_KEY = os.getenv("tweepybotck")
CONSUMER_SECRET = os.getenv("tweepybotcs")
ACCESS_TOKEN = os.getenv("tweepybotat")
ACCESS_SECRET = os.getenv("tweepybotas")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# store the AUTH details and wait parameters in to a variable to be used later.

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Below code tests the connection.
def testconnection(api):
    try:
        api.verify_credentials()
        print("Authentication is OK")
    except:
        print("Error during authentication")


# Function to get latest tweets from your twitter feed.
def getTweets(api):
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")


# Function to post a tweet on yout wall.
def putTweet(api):
    api.update_status('''
    Wish I had it all again, 
    my life wouldn't have derailed,
    Wish I had someone to say it all,
    I wouldn't be so fallen. 
''')


# Function to get search a user (public) and get its information.

def getUser(api):
    user = api.get_user("narendramodi")
    print("User details : ")
    print(user.name)
    print(user.description)
    print(user.location)
    print("Last 20 followers : ")
    for followers in user.followers():
        print(followers.name)


def addUser(api):
    friend_userName = 'narendramodi'
    friend = api.create_friendship(friend_userName)
    if friend:
        print(friend_userName + " was added")


def putLike(api):
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)


def getYourBlockedAccount(api):
    for blocks in api.blocks():
        user_name = api.get_user(blocks.id)
        print(blocks.name, "@" + user_name.screen_name)


def searchtweets(api):
    matchDict={}
    searches = api.search(q="jujutsu kaisen", lang="en", rpp="5")
    for search in searches:
        matchDict[search.user.name] = search.text

    for keys,values in matchDict.items():
        print(f"({keys} posted {values}")

def gettrends(api):
    print(api.trends_available())
    num= random.randint(0, 5)
    trends = api.trends_place(1)
    for trend in trends[0]["trends"]:
        print(trend["name"])

# getTweets(api)
# putTweet(api)
# getUser(api)
# addUser(api)
# putLike(api)
#getYourBlockedAccount(api)
#searchtweets(api)
#ettrends(api)