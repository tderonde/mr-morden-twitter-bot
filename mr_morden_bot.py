import random
import tweepy
import os
from quotes import quotes
from usernames import user_names

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

# get user id from twitter api
def get_user_id(user_name):
    response = client.get_users(usernames=user_name)
    try:
        user_id = response.data[0].id
        print(f"User {user_id} found.")
    except:
        user_id = None
        print("User not found.")
    return user_id

# get user's latest tweet (exlcuding retweets and replies) from twitter api
def get_user_tweet(user_id):
    response = client.get_users_tweets(
        user_id
        , exclude=['retweets','replies']
        , max_results=5
    )
    tweet_id = response.data[0].id
    print(f"Tweet {tweet_id} found.")
    return tweet_id

# reply to user's tweet using twitter api 
def reply_to_tweet(text, tweet_id):
    response = client.create_tweet(
        text=text
        , in_reply_to_tweet_id = tweet_id
    )
    tweet_link = f"Tweet created: https://twitter.com/user/status/{response.data['id']}"
    print(tweet_link)


## run functions to post tweet ##

# find user id for random Republican user name or B5 News and 
# will reply to this user's latest tweet
random_user_id = None
while random_user_id is None:
    random_user_name = random.choice(user_names)
    random_user_id = get_user_id(random_user_name)

# retrieve user's tweet id 
random_user_tweet_id = get_user_tweet(random_user_id)

# tweet random Morden quote to the user
quote = random.choice(quotes)
reply_to_tweet(quote, random_user_tweet_id)
