import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# config.username
# config.password

# Import Tweepy
import tweepy

import logging
import os
import pickle
import re

logger = logging.getLogger()

def create_api():


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
    except Exception as e:
        logger.err0r("Error creating API", exc_info=True)
        raise e
#         print("Error during authentication")
    logger.info("API created")
    return api

def retweet():

    # Set Authentication Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

# Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
                        wait_on_rate_limit_notify=True)
    api = tweepy.API(auth)
    url = str(input("Please enter the url of the tweet you would like retweeted."))
    id = re.findall(r'\d{19}$', url)
    api.retweet(id[0])
    print('Your tweet has been successfully retweeted!')

retweet()
