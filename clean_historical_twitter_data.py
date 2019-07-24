# -*- coding: utf-8 -*-
"""

Original file is located at
    https://colab.research.google.com/drive/1P1fiNaIbBtXux2OAfEy73t-UER6l2zOo
"""

import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.preprocessing import MinMaxScaler

x = open('twitter_03_01_2013.csv', encoding = "ISO-8859-1")
df = pd.read_csv(x)
df.head()

empty_date = df['date'].isnull().sum()
print(empty_date)

empty_username = df['username'].isnull().sum()
print (empty_username)

empty_to = df['to'].isnull().sum()
print (empty_to)

empty_replies = df['replies'].isnull().sum()
print (empty_replies)

empty_retweets = df['retweets'].isnull().sum()
print (empty_retweets)

empty_favs = df['favorites'].isnull().sum()
print (empty_favs)

empty_text = df['text'].isnull().sum()
print (empty_text)

empty_geo = df['geo'].isnull().sum()
print (empty_geo)

empty_mentions = df['mentions'].isnull().sum()
print (empty_mentions)

empty_hashtags = df['hashtags'].isnull().sum()
print(empty_hashtags)

empty_id = df['id'].isnull().sum()
print(empty_id)

empty_permalink = df['permalink'].isnull().sum()
print(empty_permalink)

df = df.drop(columns=['to', 'geo', 'mentions', 'hashtags'])

before = df.dtypes
print(before)

df['text'] = df['text'].astype('str')

after = df.dtypes
print(after)

# put each tweet in a list
columns = list(df['text'])

# initiate empty lists to store sentiment analysis - polarity and subjectivity separately
polarity_analysis_list = []
subjectivity_analysis_list = []

#for each tweet run sentiment analysis and add values to respective lists
for tweet in columns:
  blob = TextBlob(tweet)
  polarity_analysis = blob.polarity
  subjectivity_analysis = blob.subjectivity
  polarity_analysis_list.append(polarity_analysis)
  subjectivity_analysis_list.append(subjectivity_analysis)

#create new columns for polarity and subjectivty and populate it with the lists created above
df['polarity'] = polarity_analysis_list
df['subjectivity'] = subjectivity_analysis_list

# Only keep rows that don't have 0 for both their polarity and subjectivity values.
df = df[(df.polarity != 0) | (df.subjectivity != 0)]
df

#sum up the polarity and subjecitivty columns
polarity_total = df['polarity'].sum(axis=0)
subjectivity_total = df['subjectivity'].sum(axis=0) 
print(polarity_total)
print(subjectivity_total)

total_rows = df['id'].count()
print(total_rows)

polarity_avg = polarity_total / total_rows
print('polarity day average:')
print(polarity_avg)

subjectivity_avg = subjectivity_total / total_rows
print('subjectivity day average:')
print(subjectivity_avg)

# WEIGHTED SENTIMENT AVERAGES

df.dtypes

#put these values into a list for summation later
og_polarity_values = list(df['polarity'])
og_subjectivity_values = list(df['subjectivity'])
num_retweets = list(df['retweets'])
num_replies = list(df['replies'])
num_favs = list(df['favorites'])

print (num_retweets)
print (num_replies)
print (num_favs)

#adding retweets, replies, and fav values into 1 number that represents total reach of tweet
total_reach = [x+y+z for x,y,z in zip(num_retweets, num_replies, num_favs)]

#create new datafram column for total reach
df['total_reach'] = total_reach

df

#multiply original polarity score with total reach value
weighted_polarity_values = []

df['weighted_polarity'] = df['polarity']*(df['total_reach'])
#should mulitple by another constant variable because would return values greater and less than
#1 and -1, respectively??

#if there is a 0 in weighted polarity, it's because tweet had a value of 0 for total reach and 
#was multiplied by a polarity value greater than 1
#we still want to keep original polarity value
#there should be no rows with value of 0 for polarity and subjectivity
df['weighted_polarity'] = df['weighted_polarity'].replace(0, df['polarity'])

weighted_subjectivity_values = []

df['weighted_subjectivity'] = df['subjectivity']*(df['total_reach'])
#should mulitple by another constant variable because would return values greater and less than
#1 and -1, respectively??

df['weighted_subjectivity'] = df['weighted_subjectivity'].replace(0,df['subjectivity'])

df.head(10)

#DAY SENTIMENT AVERAGES

weighted_polarity_total = df['weighted_polarity'].sum(axis=0)
weighted_subjectivity_total = df['weighted_subjectivity'].sum(axis=0)
print(total_rows)
print(weighted_polarity_total)
print(weighted_subjectivity_total)

avg_w_pol = weighted_polarity_total/total_rows
avg_w_sub = weighted_subjectivity_total/total_rows

print("weighted polarity day avg:")
print(avg_w_pol)
print("\n")

print("weighted subjectivity day avg:")
print(avg_w_sub)
print("\n")

print("unweighted subjectivity day avg:")
print(subjectivity_avg)
print("\n")

print("unweighted polarity day avg:")
print(polarity_avg)

df.head(50)

scaler = MinMaxScaler(feature_range=(-1, 1))

df.columns[11:13]
weighted_data = df.as_matrix(columns=df.columns[11:13])

df[['weighted_polarity', 'weighted_subjectivity']] = scaler.fit_transform(df[['weighted_polarity', 'weighted_subjectivity']])
df.head(10)

weighted_polarity_total = df['weighted_polarity'].sum(axis=0)
weighted_subjectivity_total = df['weighted_subjectivity'].sum(axis=0)
print(total_rows)
print(weighted_polarity_total)
print(weighted_subjectivity_total)

avg_w_pol = weighted_polarity_total/total_rows
avg_w_sub = weighted_subjectivity_total/total_rows

print("weighted polarity day avg:")
print(avg_w_pol)
print("\n")

print("weighted subjectivity day avg:")
print(avg_w_sub)
print("\n")

sum(n > 0 for n in df['weighted_subjectivity'].values.flatten())

df

df.to_csv('results_10_01_2017.csv')

df.sort_values(by=['weighted_polarity'])

