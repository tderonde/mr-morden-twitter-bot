import os
import tweepy

# env variables configured in Heroku app settings
ACCESS_SECRET = os.environ["access_secret"]
ACCESS_TOKEN = os.environ["access_token"]
BEARER_TOKEN = os.environ["bearer_token"]
CONSUMER_KEY = os.environ["consumer_key"]
CONSUMER_SECRET = os.environ["consumer_secret"]

# setup tweepy client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN, 
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET
)