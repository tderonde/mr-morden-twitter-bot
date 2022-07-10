# mr-morden-bot
### Twitter bot created using Tweepy and deployed using Heroku
### https://twitter.com/MrMordenBot
* The bot tweets out a random quote or image from the character Mr. Morden from Babylon 5.
* The tweets are sent as replies to the most recent tweet from a list of Twitter accounts.
* The bot is scheduled to run daily (1 tweet per day).

<br>
<br>
Here are some tips on deploying the bot:

#### I. Twitter Developer Account Setup
1. Create project and app
2. Set up app's user authentication settings
* Enable OAuth 1.0a authentication
* Give app read-write permissions
* I set Callback URI / Redirect URL to (i) http://localhost/auth/twitter/callback and (ii) my Heroku app URL
* I set Website URL to my Twitter profile URL
3. Generate Access Token and Secret in app "Keys and tokens" tab

### II. Heroku Setup
1. Create an app and connect it to the GitHub repo that contains your code
3. In app settings, enter Twitter acess tokens/keys as config vars
* With your tokens/keys saved as Heroku config vars, you can acess them as environment variables with os.environ, like: ```ACCESS_SECRET = os.environ["access_secret"]```
* This makes it so you do not need to upload your tokens/keys to GitHub
* When setting up config vars in app settings, do not put quotes around your tokens/keys. So enter the key/token as ```abcd123efgh456789``` and not ```"abcd123efgh456789"```
4. Schedule a Job
* I'm using Heroku Scheduler to automate when my bot runs (daily).
* Because I'm using the scheduler, I do not need to use a Procfile to set a Heroku web process or worker function
<br>
<br>

#### Tweepy Docs: https://docs.tweepy.org/en/stable/
#### Heroku: https://www.heroku.com/
