import csv
from textblob import TextBlob

#infile = 'output_got.csv'
f = open('output_got.csv', 'r')
with f as csvfile:
    rows = csv.reader(csvfile)
    new_rows_list = []
    for row in rows:
        sentence = row[6]
        print (sentence)
        blob = TextBlob(sentence)
        print (blob.sentiment)
        new_rows_list.append([blob.sentiment])
f.close()

f1 = open('output_got.csv','a') 
with f1 as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(new_rows_list)
f1.close()