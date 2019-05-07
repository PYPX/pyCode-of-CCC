import json
import tweepy
import couchdb
import pickle

# In this version, the list of tweet ID will be stored in the local computer, not in the database. 
# what you shold do is :
# 1. Try to save the tweet ID in the couchdb and read the file from couchdb
# 2. Chang the filter, find a good 'geocode', which is satisfied with our need.

consumer_key = "nq7frz3elNKuDoEC2ZONfr6mb"
consumer_secret = "n4jdQbcLjvt9BXKHRZ2YXwXEQ63qrGVzOJv3KNqSPnzqek4nRO"
access_token = "1124209080820588545-wv8qh835krSB2UKgeNGca7K0MQRd0B"
access_token_secret = "KUVqGf9tH25H9Bpxef8PyFyrUzoy7qoX0p7qMc55Y5sQS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# this is use to read the file that contains all the tweet Id
try:
	id_file = open("id_list.txt", 'rb')
	id_list = pickle.load(id_file)
	id_file.close()
except:
	id_list = []

# change the data structure to set, which is easy to check duplicate
id_set = set(id_list)

# user = "VINSHON"
# password = "v021295n"
# couchserver = couchdb.Server("http://%s:%s@10.9.129.243:5984/" % (user, password))
# db = couchserver["cluster_project"]


# this try except is use to write Id to file. if the code crush, the id will be save
try:
	public_tweets = tweepy.Cursor(api.search, geocode="-37.78374010522721,144.9474334716797,100km",languages='en').items(2)
	for tweet in public_tweets:
		json_str = json.dumps(tweet._json)

		#check whether the tweet has been catched
		id = tweet.id
		if id in id_set:
			continue

		id_set.add(id)
		#db.save(json_str)
except:
	id_list = list(id_set)
	id_file = open("id_list.txt", 'wb')
	pickle.dump(id_list, id_file)
	id_file.close()



