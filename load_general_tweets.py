import tweepy
from db_utils import db_connect
import sqlite3
import json
import re
from textblob import TextBlob
import pandas as pd

def clean_text(message):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", message).split())

consumer_key = 'iYuXDDCGpHK21IKsdPHp2SGyC'
consumer_secret = 'WS0VRAEgucLPMUC4sPHkR6paNWUWjnQMD9Sa69dLMsbYnSoGSl'
access_token = '1059635773832654849-dXbjvut3bhqxSiz3ELj1mVW3PN6qXR'
access_token_secret = 'xDOSZMwZkBZrlDMjrVA7liAcnS0zCxu6qchzqdOOJr6AL'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

con = db_connect()
cur = con.cursor()

count = 0

general_sql = "INSERT INTO general_tweets (tweet_message, polarity, subjectivity, sentiment) VALUES (?, ?, ?, ?)"

for tweet in tweepy.Cursor(api.search, lang='en', q="a").items():
	analysis = TextBlob(clean_text(tweet.text))
	polarity = analysis.sentiment.polarity
	subjectivity = analysis.sentiment.subjectivity
	if polarity > 0 :
		sentiment = 'positive'
	elif polarity < 0:
		sentiment = 'negative'
	else:
		sentiment = 'neutral'
	cur.execute(general_sql, (tweet.text, polarity, subjectivity, sentiment))
	count = count + 1
	if count > 10000: break