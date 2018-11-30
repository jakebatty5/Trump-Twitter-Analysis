from db_utils import db_connect
import sqlite3
import json
import re
from textblob import TextBlob
import pandas as pd
import tweepy
import config

def clean_text(message):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", message).split())

def load_response_no_keywords():
	response_no_keywords_sql = "INSERT INTO response_no_keywords (tweet_message, polarity, subjectivity, sentiment) VALUES (?, ?, ?, ?)"

	count = 0

	for tweet in tweepy.Cursor(api.search, lang='en', q="@realDonaldTrump").items():
		analysis = TextBlob(clean_text(tweet.text))
		polarity = analysis.sentiment.polarity
		subjectivity = analysis.sentiment.subjectivity
		if polarity > 0 :
			sentiment = 'positive'
		elif polarity < 0:
			sentiment = 'negative'
		else:
			sentiment = 'neutral'
		cur.execute(response_no_keywords_sql, (tweet.text, polarity, subjectivity, sentiment))
		count = count + 1
		if count > 100: break

	con.commit()

def load_response_pos_keywords():
	response_pos_keywords_sql = "INSERT INTO response_pos_keywords (keyword, tweet_message, polarity, subjectivity, sentiment) VALUES (?, ?, ?, ?, ?)"
	pos_keywords = ['big','tax','today','many','thank','more','people','very','america','great']

	for keyword in pos_keywords:
		count = 0
		for tweet in tweepy.Cursor(api.search, lang='en', q='@realDonaldTrump %s'%(keyword)).items():
			analysis = TextBlob(clean_text(tweet.text))
			polarity = analysis.sentiment.polarity
			subjectivity = analysis.sentiment.subjectivity
			if polarity > 0 :
				sentiment = 'positive'
			elif polarity < 0:
				sentiment = 'negative'
			else:
				sentiment = 'neutral'
			cur.execute(response_pos_keywords_sql, (keyword, tweet.text, polarity, subjectivity, sentiment))
			count = count + 1
			if count > 100: break
	con.commit()

def load_response_neg_keywords():
	response_neg_keywords_sql = "INSERT INTO response_neg_keywords (keyword, tweet_message, polarity, subjectivity, sentiment) VALUES (?, ?, ?, ?, ?)"
	neg_keywords = ['country','big','bad','now','very','trump','people','media','news','fake']

	for keyword in neg_keywords:
		count = 0
		for tweet in tweepy.Cursor(api.search, lang='en', q='@realDonaldTrump %s'%(keyword)).items():
			analysis = TextBlob(clean_text(tweet.text))
			polarity = analysis.sentiment.polarity
			subjectivity = analysis.sentiment.subjectivity
			if polarity > 0 :
				sentiment = 'positive'
			elif polarity < 0:
				sentiment = 'negative'
			else:
				sentiment = 'neutral'
			cur.execute(response_neg_keywords_sql, (keyword, tweet.text, polarity, subjectivity, sentiment))
			count = count + 1
			if count > 100: break
	con.commit()

con = db_connect()
cur = con.cursor()
auth = tweepy.OAuthHandler(config.consumer_key(), config.consumer_secret())
auth.set_access_token(config.access_token(), config.access_token_secret())
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

con.close()