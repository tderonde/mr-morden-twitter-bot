import os
import tweepy

# env variables configured in Heroku app settings
ACCESS_SECRET = os.environ["access_secret"]
ACCESS_TOKEN = os.environ["access_token"]
BEARER_TOKEN = os.environ["bearer_token"]
CONSUMER_KEY = os.environ["consumer_key"]
CONSUMER_SECRET = os.environ["consumer_secret"]

# setup client for twitter api v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN, 
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET
)

# set up for twitter api v1.1
# there is currently no media upload endpoint for v2 
# so need to use v1.1 endpoint
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
)
api = tweepy.API(auth)