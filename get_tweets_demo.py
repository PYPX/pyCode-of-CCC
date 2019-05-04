import json
import tweepy

consumer_key = "nq7frz3elNKuDoEC2ZONfr6mb"
consumer_secret = "n4jdQbcLjvt9BXKHRZ2YXwXEQ63qrGVzOJv3KNqSPnzqek4nRO"
access_token = "1124209080820588545-wv8qh835krSB2UKgeNGca7K0MQRd0B"
access_token_secret = "KUVqGf9tH25H9Bpxef8PyFyrUzoy7qoX0p7qMc55Y5sQS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def parse(status):
	json_str = json.dumps(status._json)
	data = json.loads(json_str)
	creatTime = data['created_at']
	twitterId = data['id']
	text = data['text']
	userId = data['user']['id']
	try:
		coordinates = data['place']['bounding_box']['coordinates']
	except:
		coordinates = "There are no coordinates in this twitter"
	# need try except
	f = open("parsed_data_demo.txt", "a")
	strData = str(creatTime) +'    '+ str(twitterId) +'    '+ text +'    '+ str(userId) +'    '+ str(coordinates) + '\n'
	print (type(strData))
	print(data['place'])
	f.write(str(data))
	f.write('\n')
	f.close()



public_tweets = api.user_timeline('133880286')
for tweet in public_tweets:
	parse(tweet)


# for status in tweepy.Cursor(api.user_timeline).items():
# 	print (type(status))
# 	json_str = json.dumps(status._json)
# 	print(type(json_str))
# 	print(json_str)
# 	json.dumps(status)
# 	print(type(status))
# 	break



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


# Step 2: Creating a Stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)


# Step 3: Starting a Stream
# myStream.filter(locations=[130.51,-25.07,146.38,-24.30])
# myStream.filter(track=['python'])
# myStream.filter(follow=["2211149702"])







