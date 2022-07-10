from tweepy_client import client

# get user id from twitter api
def get_user_id(user_name):
    user_id = None
    i = 0
    while user_id == None and i < 5:
        print(f"Running {get_user_id.__name__}({user_name})...")
        response = client.get_users(usernames=user_name)
        try:
            user_id = response.data[0].id
            print(f"Success. User ID {user_id} found.")
        except:
            user_id = None
            print(f"Error.")
        i += 1
    
    return user_id

if __name__ == "__main__":
    get_user_id('MrMordenBot')