import tweepy

consumer_key = "Di2t90Ru7HvBl02JqFhtt3SAE"
consumer_secret = "s02nhrpmXE441MzWzEx5noYkc2V0zYBGvFuNPxtvPsxip8he7x"
atoken = "3731913556-aDibg2miti6XsIHIIUanQCrQRBJBcv4FFcxd1sR"
asecret = "fCmuUCy5pjyiyL6nPr2ANMk4hg3wuGl9m57KaWrXK4usa"

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

results = api.search("#happy")

print results[1]
