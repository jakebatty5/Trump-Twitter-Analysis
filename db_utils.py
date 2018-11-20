import os  
import sqlite3

# create a default path to connect to
# called 'tweet_db.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'tweet_db.sqlite3')

def db_connect(db_path=DEFAULT_PATH):  
    con = sqlite3.connect(db_path)
    return con