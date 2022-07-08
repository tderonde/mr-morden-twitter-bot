import random

from quotes import quotes
from usernames import user_names
from tweepy_client import client, api
from get_user_id import get_user_id
from get_user_tweet import get_user_tweet
from send_tweet import send_tweet

## run functions to post tweet ##

i = 0
tweet_link = None

while tweet_link == None and i < 5:
    print("Starting...")
    # find user id for random Republican user name or B5 News 
    random_user_name = random.choice(user_names)
    random_user_id = get_user_id(random_user_name)

    # retrieve random user's tweet id 
    random_user_tweet_id = get_user_tweet(random_user_id)

    # reply to the random user's most recent tweet with a random Mr. Morden quote
    quote = random.choice(quotes)
    if quote and random_user_tweet_id:
        tweet_link = send_tweet(quote, random_user_tweet_id)
    else:
        print("Retrying...")
    i += 1
    