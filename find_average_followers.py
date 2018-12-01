from db_utils import db_connect
import sqlite3
import config
import tweepy

con = db_connect() #connect to db
cur = con.cursor() #instantiate cursor object

auth = tweepy.OAuthHandler(config.consumer_key(), config.consumer_secret())
auth.set_access_token(config.access_token(), config.access_token_secret())

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

collect_followers_sql = '''
CREATE TABLE collect_followers (
	id integer PRIMARY KEY,
	userid integer NOT NULL,
	followers integer NOT NULL)'''

#cur.execute(collect_followers_sql)

load_collect_followers_sql = "INSERT INTO collect_followers (userid, followers) VALUES (?, ?)"

count = 0
for tweet in tweepy.Cursor(api.search, q="a").items():
	count = count+1
	cur.execute(load_collect_followers_sql,(tweet.id, tweet._json['user']['followers_count']))
	if count>2000: break

con.commit()
con.close()