# get user id from twitter api
def get_user_id(user_name):
    print(f"Running {get_user_id.__name__}({user_name})...")
    response = client.get_users(usernames=user_name)
    try:
        user_id = response.data[0].id
        print(f"Success. User ID {user_id} found.")
    except:
        user_id = None
        print(f"Error.")
    return user_id

if __name__ == "__main__":
    from tweepy_client import client
    get_user_id('MrMordenBot')