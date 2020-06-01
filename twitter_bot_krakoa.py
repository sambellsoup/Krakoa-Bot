import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
# config.username
# config.password

# Import Tweepy
import tweepy

# Set Authentication Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Create API Object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



# Creates a new tweet
# .update_status("Tweet")

# api.update_status("Test tweet from Tweepy Python")

# Retweet that Tweet!

# Tweepy provides HTTP endpoints for:
# Tweets
# Retweets
# Likes
# Direct messages
# Favorites
# Trends
# Media

# Methods for User Timelines

# timeline = api.home_timeline()
# for tweet in timeline:
    # print(f"{tweet.user.name} said {tweet.text}")


# Methods for Tweets
# api.update_status("Test tweet from Tweepy Python")

# Methods for Users
# user = api.get_user("MikezGarcia")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
    # print(follower.name)

# Methods for Following Users
# api.create_friendship("realpython")

# Methods for your account
# api.update_profile(description="I like Python")



# Tweepy requires that all requests use OAuth to authenticate.
# So you need to create the required authentication credentials to be able to use the API.

# These credentials are four text strings:

# Consumer key
# Consumer secret
# Access token
# Access secret
