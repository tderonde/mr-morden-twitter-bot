from tweepy_client import client, api

# send tweet or reply to user's tweet using twitter api 
def send_tweet(text, tweet_id=None, media_id=None):
    print(f"Running {send_tweet.__name__}({text, tweet_id})...")
    try:
        response = client.create_tweet(
            text=text
            , in_reply_to_tweet_id = tweet_id
            , media_ids=[media_id]
        )
        tweet_link = f"Tweet created: https://twitter.com/user/status/{response.data['id']}"
        print(tweet_link)
    except:
        tweet_link = None
        print(f"Error.")
    return tweet_link

if __name__ == "__main__":
    media = api.simple_upload("images/1.png")
    media_id = media.media_id
    send_tweet("Hello.", 1541147179426861056, media_id)
