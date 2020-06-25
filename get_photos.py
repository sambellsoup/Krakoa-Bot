import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# config.username
# config.password

from outboard_scrape import rand_user_agent

# Internets navigation
# from urllib.request import Request, urlopen

# Scraping tool
from bs4 import BeautifulSoup

# Import Tweepy
import tweepy

import pandas as pd
import re
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set Authentication Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
def create_api():
# Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
                        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        logger.err0r("Error creating API", exc_info=True)
        raise e
        print("Error during authentication")

create_api()

# Collect the usernames of all followers
import tweepy

def get_followers():
    my_followers = []
    for follower in tweepy.Cursor(api.followers, screen_name='KrakoaWelcomes').items():
        my_followers.append(follower.screen_name)
        time.sleep(1)

get_followers()

html_tobeparsed = []
n= 0
i = 1

# source_code = requests.get('http://fantasy.espn.com/basketball/league/standings?leagueId=633975')
def get_html():
    for follower in my_followers.followers:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        capa = DesiredCapabilities.CHROME
        capa["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome(options=options, desired_capabilities=capa)
        driver.set_window_size(1440,900)
        driver.get('https://twitter.com/' + my_followers.followers[n] + '/photo')
        print('getting user #' + str(i) + "'s photo url!")
        time.sleep(15)

        plain_text = driver.page_source
        new_soup = BeautifulSoup(plain_text, 'lxml')
        pattern = re.compile('draggable="true" src="(.*).+?(?=\/>)')
        html_tobeparsed.extend(new_soup)
        print("html added")
        n+=1
        i+=1
    print("all done!")

def parse_url():
    i = 0
    for text in my_followers.html:
        url = re.findall('url\(\"(.+?)(?=\")', my_followers.html[i])
        if url == []:
            file_url.extend(' ')
            print(str(i) + ' ' + my_followers.followers[i] + "'s photo did not work!")
        else:
            file_url.extend(url)
        i += 1
parse_url()

def get_photos():

    i = 1
    try:
        for url in new_urls:
            f = open(str(i) + '.jpg','wb')
            f.write(requests.get(url).content)
            f.close()
            i += 1
    except HTTPError as err:
        if err.code == 404:
            print(str(url) + " was not found!")
            pass 
