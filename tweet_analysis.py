from db_utils import db_connect
import sqlite3
import config

con = db_connect() #connect to db
cur = con.cursor() #instantiate cursor object

#percent pos/neg/neutral
positive_trump_tweets = cur.execute("SELECT COUNT(polarity) FROM trump_tweets WHERE sentiment='positive'").fetchall()[0][0]
negative_trump_tweets = cur.execute("SELECT COUNT(polarity) FROM trump_tweets WHERE sentiment='negative'").fetchall()[0][0]
neutral_trump_tweets = cur.execute("SELECT COUNT(polarity) FROM trump_tweets WHERE sentiment='neutral'").fetchall()[0][0]
total_trump_tweets = cur.execute("SELECT COUNT(polarity) FROM trump_tweets").fetchall()[0][0]
print("Percent of positive Trump tweets: ", round(positive_trump_tweets/total_trump_tweets*100,1),"%")
print("Percent of negative Trump tweets: ", round(negative_trump_tweets/total_trump_tweets*100,1),"%")
print("Percent of neutral Trump tweets: ", round(neutral_trump_tweets/total_trump_tweets*100,1),'%\n')

positive_general_tweets = cur.execute("SELECT COUNT(polarity) FROM general_tweets WHERE sentiment='positive'").fetchall()[0][0]
negative_general_tweets = cur.execute("SELECT COUNT(polarity) FROM general_tweets WHERE sentiment='negative'").fetchall()[0][0]
neutral_general_tweets = cur.execute("SELECT COUNT(polarity) FROM general_tweets WHERE sentiment='neutral'").fetchall()[0][0]
total_general_tweets = cur.execute("SELECT COUNT(polarity) FROM general_tweets").fetchall()[0][0]
print("Percent of positive public tweets: ", round(positive_general_tweets/total_general_tweets*100,1),"%")
print("Percent of negative public tweets: ", round(negative_general_tweets/total_general_tweets*100,1),"%")
print("Percent of neutral public tweets: ", round(neutral_general_tweets/total_general_tweets*100,1),"%\n")

#average polarity scores
cur.execute("SELECT AVG(polarity) FROM trump_tweets")
print("Average polarity of Trump tweets: ", round(cur.fetchall()[0][0],2))
cur.execute("SELECT AVG(polarity) FROM general_tweets")
print("Average polarity of general public tweets: ", round(cur.fetchall()[0][0],2))
cur.execute("SELECT COUNT(polarity) FROM trump_tweets")
print("Number of Trump tweets analyzed: ", cur.fetchall()[0][0])
cur.execute("SELECT COUNT(polarity) FROM general_tweets")
print("Number of general public tweets analyzed: ", cur.fetchall()[0][0],'\n')

#average sentiment, polarity in response to trump in general, and to pos/neg keywords
polarity_no_keyword = cur.execute("SELECT AVG(polarity) FROM response_no_keywords").fetchall()[0][0]
sample_no_keyword = cur.execute("SELECT COUNT(polarity) FROM response_no_keywords").fetchall()[0][0]

polarity_pos_keyword = cur.execute("SELECT AVG(polarity) FROM response_pos_keywords").fetchall()[0][0]
sample_pos_keyword = cur.execute("SELECT COUNT(polarity) FROM response_pos_keywords").fetchall()[0][0]

polarity_neg_keyword = cur.execute("SELECT AVG(polarity) FROM response_neg_keywords").fetchall()[0][0]
sample_neg_keyword = cur.execute("SELECT COUNT(polarity) FROM response_neg_keywords").fetchall()[0][0]

print("Average polarity of tweets mentioning Trump: ", round(polarity_no_keyword,2))
print("Average polarity of tweets mentioning Trump with positive keywords: ", round(polarity_pos_keyword,2))
print("Average polarity of tweets mentioning Trump with negative keywords: ", round(polarity_neg_keyword,2),'\n')
print("Sample size of tweets mentioning Trump: ", sample_no_keyword)
print("Sample size of tweets mentioning Trump with positive keywords: ", sample_pos_keyword)
print("Sample size of tweets mentioning Trump with negative keywords: ", sample_neg_keyword)

con.close()


#identify keywords that had most neg/positive response from public
#visual- average polarity per keyword. two charts, one for pos and one for neg keywords, keywords listed in order of prevelance from trump tweets

#stream as many random tweets as possible, store number of users for each, take the averagef