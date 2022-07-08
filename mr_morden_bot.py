import random

from quotes import quotes
from usernames import user_names
from png_filenames import png_filenames
from tweepy_client import api
from get_user_id import get_user_id
from get_user_tweet import get_user_tweet
from send_tweet import send_tweet

## run functions to post tweet ##

i = 0
tweet_link = None

while tweet_link == None and i < 5:
    print("Starting...")
    # find user id for random Republican user name or B5 News 
    user_name = random.choice(user_names)
    user_id = get_user_id(user_name)

    # retrieve random user's tweet id 
    tweet_id = get_user_tweet(user_id)

    # reply to the random user's most recent tweet with a random Mr. Morden quote or image
    tweet_list = list(zip(quotes, ['text'] * len(quotes))) + list(zip(png_filenames, ['png'] * len(png_filenames)))
    tweet = random.choice(tweet_list)

    if tweet and tweet_id:
        if tweet[1] == 'text':
            text = tweet[0]
            media_id = None
        else:
            text = None
            media = api.simple_upload(tweet[0])
            media_id = media.media_id
        tweet_link = send_tweet(text, tweet_id, media_id)
    else:
        print("Retrying...")
    i += 1
    