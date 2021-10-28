import tweepy
from keys import keys
consumer_key='eAOfFzJgH2ztOkk6wAHmmBU9t'
consumer_secret='tl7JVTgZHHi1l7yXlsq3IEbGGzDyyuZvHoVlfUKOZA2m6s5zyn'

access_token ='706257275-cyX75ztH6NzrsK5euyVKARXFCtyxGz5lxU6k8DFI'
access_token_secret ='ZPD9pzLTYtALp8cwChPkev1Lp5Puna0LR4pjo4fafY2IJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Test Tweet erzeugen
tweet = "Hello World!"
api.update_status(status=tweet)
print()

