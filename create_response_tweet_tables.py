from db_utils import db_connect
import sqlite3

con = db_connect() #connect to db
cur = con.cursor() #instantiate cursor object

response_no_keywords_sql = '''
CREATE TABLE response_no_keywords (
	id integer PRIMARY KEY,
	tweet_message text NOT NULL,
	polarity real NOT NULL,
	subjectivity real NOT NULL,
	sentiment text NOT NULL)'''

response_pos_keywords_sql = '''
CREATE TABLE response_pos_keywords (
	id integer PRIMARY KEY,
	keyword text NOT NULL,
	tweet_message text NOT NULL,
	polarity real NOT NULL,
	subjectivity real NOT NULL,
	sentiment text NOT NULL)'''

response_neg_keywords_sql = '''
CREATE TABLE response_neg_keywords (
	id integer PRIMARY KEY,
	keyword text NOT NULL,
	tweet_message text NOT NULL,
	polarity real NOT NULL,
	subjectivity real NOT NULL,
	sentiment text NOT NULL)'''

cur.execute(response_no_keywords_sql)
cur.execute(response_pos_keywords_sql)
cur.execute(response_neg_keywords_sql)

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

con.close()