import tweepy
from tweepy import Stream
from tweepy import StreamListener 
from tweepy import OAuthHandler
import json
import couchdb
import pandas as pd

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

rows = db.view('_all_docs', include_docs=True)
for row in rows:
    data = row['doc']
    print(data['_id'])
    #df = pd.DataFrame(data)
    #print(df['_id'])
#data = [row['doc'] for row in rows]
#df = pd.DataFrame(data)
#print(df['_id'])