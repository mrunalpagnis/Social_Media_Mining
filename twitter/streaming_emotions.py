import tweepy
from tweepy import Stream
import StreamListenerClass as strm
import time

seeds = ["#disgusted", "#fearful", "#angry", "#surprised", "#scared", "#lonely", "#excited", "#wonderful", "#sleepy"]

"""
authenticates into the twitter API using the authentication handler and returns the authentication object
For generating the keys follow link: https://www.apps.twitter.com

1.Generate the Consumer key and consumer secret
2.You will now find a button on screen below your consumer secret key that says generate "access token". 
3.Go ahead and generate your access token.
4.Copy and paste those in your code.

"""
def authenticate():
    
    consumer_key = "Di2t90Ru7HvBl02JqFhtt3SAE"
    consumer_secret = "s02nhrpmXE441MzWzEx5noYkc2V0zYBGvFuNPxtvPsxip8he7x"
    
    atoken = "3731913556-aDibg2miti6XsIHIIUanQCrQRBJBcv4FFcxd1sR"
    asecret = "fCmuUCy5pjyiyL6nPr2ANMk4hg3wuGl9m57KaWrXK4usa"
    
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(atoken, asecret)
    
    return auth
    
    
"""
use the auth object to initialize the stream and then specify the filter to extract data from twitter
"""

def listen_to_stream(auth):
    
    twitter_stream = Stream(auth,strm.listener(time.time(),20000))
    twitter_stream.filter(track = seeds, languages = ['en'])
    
if __name__ == '__main__':
    
    listen_to_stream(authenticate())
    