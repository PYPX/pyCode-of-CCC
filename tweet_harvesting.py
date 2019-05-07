import json
import tweepy
import couchdb


access_token = "1655276844-Rbjk1jjqYdr5gzcEyOjcCAkYfzZ0ZP9gUzPwGUY"
access_token_secret = "hFll6jNnGOpHLC4Nnq96YL9nxhD5peYLe0w5dq7EYXURB"
consumer_key = "3KZFaT7v2JzvUZPq3WbQjd6l1"
consumer_secret = "827ZUNUmysKigqGYwcr2Z0PbUeoS1ZNQiCZ32Q1d2G4v44bP5K"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = "VINSHON"
password = "v021295n"
couchserver = couchdb.Server("http://%s:%s@10.9.129.243:5984/" % (user, password))
db = couchserver["cluster_project"]





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
	def on_status(self, data):
		try:
			file1 = json.dumps(data)
			db.save(file1)
			print("Inserted")
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print(status)
		return True


# Step 2: Creating a Stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(locations=[130.51,-25.07,146.38,-24.30])