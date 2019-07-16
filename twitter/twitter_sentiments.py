import tweepy
from textblob import TextBlob
import csv
import datetime
import pandas as pd
import numpy as np

# Unique code from Twitter
access_token = "YOUR CODE"
access_token_secret = "YOUR CODE"
consumer_key = "YOUR CODE"
consumer_secret = "YOUR CODE"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('Bitcoin')

f = open('hi.csv', 'a')
with f as scorefile:
	scoreFileWriter = csv.writer(scorefile)
	for tweet in public_tweets:
		tweet_text = tweet.text
		analysis = TextBlob(tweet.text)
		analysis_sentiment = analysis.sentiment
		current = str(datetime.datetime.today())
		scoreFileWriter.writerow([tweet_text,analysis_sentiment,current])



#f = open('twitter.csv','w')
# with open('twitter.csv', 'w') as scorefile:
#     scoreFileWriter = csv.writer(scorefile) 
#     for tweet in public_tweets:
#     	tweet_text = tweet.text
# 		# print(tweet_text)
# 		analysis = TextBlob(tweet.text)
# 		analysis_sentiment = analysis.sentiment
# 		# analysis_sentiment = str(analysis_sentiment)
# 		# print (analysis_sentiment)
# 		# f.write(tweet_text)
# 		# f.write('\t')
# 		# #f.write(analysis_sentiment)
# 		# current = datetime.datetime.today()
# 		# print (current)
# 		# f.write('\t')
# 		# f.write(str(current))
# 		# f.write('\n')
# 		scoreFileWriter.writerow([tweet_text,analysis_sentiment])




#polarity -- measures how positive or negative
#subjectivity -- measures how factual.
#1 Sentiment Analysis - Understand and Extracting Feelings from Data

# infile = 'twitter.csv'
# analysislist = list()

# with open(infile, 'r') as csvfile:
#     rows = csv.reader(csvfile)

# for row in rows:
#     sentence = row[0]
#     blob = TextBlob(sentence)
#     bloblist.append((sentence,blob.sentiment.polarity, blob.sentiment.subjectivity))

# df = pd.DataFrame(bloblist, columns = ['sentence','sentiment','polarity'])

