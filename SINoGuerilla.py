
from Keys import consumer_key, consumer_secret, bearer_token, access_token, access_secret
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
auth.secure = True
api = tweepy.API(auth)

print(str(api.get_user(screen_name = '@neatobrumf')))