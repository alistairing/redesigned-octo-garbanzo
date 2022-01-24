import tweepy
import os

# Get API keys and secrets

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET,
                       bearer_token=BEARER_TOKEN)

response = client.create_tweet(text='hello world')

print(response)
