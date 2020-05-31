import config

config.consumer_key
config.consumer_secret
config.access_token
config.access_token_secret
config.username
config.password

# Import Tweepy
import tweepy

# Set Authentication Credentials
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API Object
api = tweepy.API(auth)

# Creates a new tweet
# .update_status("Tweet")

api.update_status("ACAB")

# Retweet that Tweet!

# Tweepy provides HTTP endpoints for:
# Tweets
# Retweets
# Likes
# Direct messages
# Favorites
# Trends
# Media

# Tweepy requires that all requests use OAuth to authenticate.
# So you need to create the required authentication credentials to be able to use the API.

# These credentials are four text strings:

# Consumer key
# Consumer secret
# Access token
# Access secret
