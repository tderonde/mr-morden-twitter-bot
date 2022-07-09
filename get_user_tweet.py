from tweepy_client import client

# get user's latest tweet (exlcuding retweets & replies) from twitter api
def get_user_tweet(user_id):
    print(f"Running {get_user_tweet.__name__}({user_id})...")
    response = client.get_users_tweets(
        user_id
        , exclude=['retweets','replies']
        , max_results=5
    )
    try:
        tweet_id = response.data[0].id
        print(f"Success. Tweet {tweet_id} found.")
    except:
        tweet_id = None
        print(f"Error.")
    return tweet_id

if __name__ == "__main__":
    get_user_tweet(1541058121711308802)
