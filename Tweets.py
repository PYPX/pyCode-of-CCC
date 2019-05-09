import tweepy
from tweepy import Stream
from tweepy import StreamListener 
from tweepy import OAuthHandler
import json
import couchdb

# Twitter API Key 
access_token = "1655276844-Rbjk1jjqYdr5gzcEyOjcCAkYfzZ0ZP9gUzPwGUY"
access_secret = "hFll6jNnGOpHLC4Nnq96YL9nxhD5peYLe0w5dq7EYXURB"
consumer_key = "3KZFaT7v2JzvUZPq3WbQjd6l1"
consumer_secret = "827ZUNUmysKigqGYwcr2Z0PbUeoS1ZNQiCZ32Q1d2G4v44bP5K"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# DB credentials
user = "VINSHON"
password = "v021295n"
couchserver = couchdb.Server("http://%s:%s@10.9.128.11:5984/" % (user, password))
db = couchserver["cluster_project"]

public_tweets = tweepy.Cursor(api.search, geocode="-37.78374010522721,144.9474334716797,100km",languages='en').items(2000)
for tweet in public_tweets:
	data = json.dumps(tweet._json)
	file1 = json.loads(data)
	#print(type(file1))
	#file1 = json.dumps(tweet)
	db.save(file1)
	#f = open("/Users/haritabala/UnimelbSem1/ClusterCloud/Assignment2/json_files/testTweet_1.json", "a")
	#db.save(data)
	#f.write(data)
	#f.write('\n')
	#f.close()
# for status in tweepy.Cursor(api.user_timeline).items():
# 	print (type(status))
# 	json_str = json.dumps(status._json)
# 	print(type(json_str))
# 	print(json_str)
# 	json.dumps(status)
# 	print(type(status))
# 	break


# the step 1,2,3 is a realtime tweeets grab function
# step 1: Creating a StreamListener
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		parse(status)

	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_error disconnects the stream
			print(status_code)
			return False
		else :
			print(status_code)
			return True


