from db_utils import db_connect
import sqlite3

con = db_connect() #connect to db
cur = con.cursor() #instantiate cursor object

proceed = input("Enter 'yes' in order to create tables:\n")

if proceed == 'yes':

	general_tweets_sql = '''
	CREATE TABLE general_tweets (
		id integer PRIMARY KEY,
		tweet_message text NOT NULL,
		polarity real NOT NULL,
		subjectivity real NOT NULL,
		sentiment text NOT NULL)'''

	trump_tweets_sql = '''
	CREATE TABLE trump_tweets (
		id integer PRIMARY KEY,
		tweet_message text NOT NULL,
		polarity real NOT NULL,
		subjectivity real NOT NULL,
		sentiment text NOT NULL)'''

	trump_responses_sql = '''
	CREATE TABLE trump_responses (
		id integer PRIMARY KEY,
		tweet_message text NOT NULL,
		polarity real NOT NULL,
		subjectivity real NOT NULL,
		sentiment text NOT NULL)'''

	cur.execute(general_tweets_sql)
	cur.execute(trump_tweets_sql)
	cur.execute(trump_responses_sql)

con.close()