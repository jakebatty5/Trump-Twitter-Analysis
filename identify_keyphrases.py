from db_utils import db_connect
import sqlite3

#make single list of words used
def compile_text(text):
	compiled_text = []
	for line in text:
		line = line.split(" ")
		for word in line:
			compiled_text.append(word.lower())
	return compiled_text

#Remove same stopwords as used by MySQL, with addition of RT and amp
def identify_keywords(words_list):
	stop_words = ["a","able","about","across","after","all","almost","also","am","amp","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your","ain't","aren't","can't","could've","couldn't","didn't","doesn't","don't","hasn't","he'd","he'll","he's","how'd","how'll","how's","i'd","i'll","i'm","i've","isn't","it's","might've","mightn't","must've","mustn't","rt", "shan't","she'd","she'll","she's","should've","shouldn't","that'll","that's","there's","they'd","they'll","they're","they've","wasn't","we'd","we'll","we're","weren't","what'd","what's","when'd","when'll","when's","where'd","where'll","where's","who'd","who'll","who's","why'd","why'll","why's","won't","would've","wouldn't","you'd","you'll","you're","you've"]
	word_count = {}
	for word in words_list:
		if word in stop_words or len(word)==1:
			continue
		if word in word_count:
			word_count[word] = word_count[word]+1
		else:
			word_count[word] = 1
	sorted_by_value = sorted(word_count.items(), key=lambda kv: kv[1])
	return str(sorted_by_value[-10:])

con = db_connect()
cur = con.cursor()

data = cur.execute("SELECT tweet_message FROM trump_tweets")
text = [x[0] for x in data]
text = compile_text(text)
file = open("keywords_all.txt","w")
file.write(identify_keywords(text))
file.close()

data = cur.execute("SELECT tweet_message FROM trump_tweets WHERE sentiment='negative'")
text = [x[0] for x in data]
text = compile_text(text)
file = open("keywords_negative.txt","w")
file.write(identify_keywords(text))
file.close()

data = cur.execute("SELECT tweet_message FROM trump_tweets WHERE sentiment='positive'")
text = [x[0] for x in data]
text = compile_text(text)
file = open("keywords_positive.txt","w")
file.write(identify_keywords(text))
file.close()


con.close()