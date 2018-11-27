from db_utils import db_connect
import sqlite3
import json
import re
from textblob import TextBlob
import pandas as pd

def clean_text(message):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", message).split())

con = db_connect()
cur = con.cursor()
trump_sql = "INSERT INTO trump_tweets (tweet_message, polarity, subjectivity, sentiment) VALUES (?, ?, ?, ?)"

proceed = input('Enter yes to reload trump_tweets:\n')
if proceed == 'yes':
	with open('condensed_2017.json') as json_file:
		seventeen_data = json.load(json_file)

	with open('condensed_2018.json') as json_file:
		eighteen_data = json.load(json_file)

	for line in seventeen_data:
		message = clean_text(line['text'])
		analysis = TextBlob(message)
		polarity = analysis.sentiment.polarity
		subjectivity = analysis.sentiment.subjectivity
		if polarity > 0 :
			sentiment = 'positive'
		elif polarity < 0:
			sentiment = 'negative'
		else:
			sentiment = 'neutral'
		cur.execute(trump_sql, (message, polarity, subjectivity, sentiment))

	for line in eighteen_data:
		message = clean_text(line['text'])
		analysis = TextBlob(message)
		polarity = analysis.sentiment.polarity
		subjectivity = analysis.sentiment.subjectivity
		if polarity > 0 :
			sentiment = 'positive'
		elif polarity < 0:
			sentiment = 'negative'
		else:
			sentiment = 'neutral'
		cur.execute(trump_sql, (message, polarity, subjectivity, sentiment))
	con.commit()
cur.execute("SELECT * from trump_tweets")
print(cur.fetchall())
con.close()

