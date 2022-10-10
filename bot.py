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

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class ClassStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        user = client.get_user(id = tweet.author_id)
        print("@"+ str(user.data) + " --- "  + tweet.text)
        try:
            client.retweet(tweet.id)
        except tweepy.errors.TooManyRequests as tooManyRequests:
            print("Parando o bot durante 30 segundos devido a excessivas requisições!")
            print(tooManyRequests)
            sleep(30)
        except Exception as error:
            print(error)

stream = ClassStream(bearer_token=BEARER_TOKEN)
regra = tweepy.StreamRule("couve -is:retweet -is:quote -is:reply")

print("Stream rodando!")
stream.filter(tweet_fields=['author_id', 'edit_history_tweet_ids', 'id', 'text'])
