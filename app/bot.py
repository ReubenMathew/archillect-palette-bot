# settings.py
from os.path import join, dirname
import os
from dotenv import load_dotenv
 
# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

apiKey = os.getenv('TWITTER_API_KEY')
apiSecret = os.getenv('TWITTER_API_SECRET')
accessToken = os.getenv('TWITTER_ACCESS_TOKEN')
accessSecret = os.getenv('TWITTER_ACCESS_SECRET')

import datetime
import io
import json
import os
import queue

import requests
import tweepy


auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken,accessSecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user_id = 2907774137

class ResponseTweet:
    def __init__(self, text, in_response):
        self.text = text
        self.in_response = in_response

class TweetStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if (status.user.id == user_id) and 'media' in status.entities and not hasattr(status, 'retweeted_status'):
            image = status.entities['media'][0]['media_url']
            print(image, status.id)
            # api.update_status("Color Palette", in_reply_to_status_id=status.id,media_ids=[image])

tweetStreamListener = TweetStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=tweetStreamListener)
myStream.filter(follow=[str(user_id)])