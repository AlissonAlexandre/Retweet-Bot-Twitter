import os
from dotenv import load_dotenv
import tweepy
from time import sleep

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class ClassStream(tweepy.StreamingClient):
    def on_tweet(selft, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)
        except tweepy.errors.TooManyRequests as tooManyResquests:
            print("Parando o bot durante 30 segundo devido a excessivas requisições!")
            sleep(30)
        except Exception as error:
            print(error)

stream = ClassStream(bearer_token=BEARER_TOKEN)
regra = tweepy.StreamRule("couve")
stream.add_rules(regra, dry_run=True)
print("Stream rodando!")
stream.filter()
