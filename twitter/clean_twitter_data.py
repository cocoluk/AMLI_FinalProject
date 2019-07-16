import pandas as pd
import numpy as np

df = pd.read_csv('hi.csv')
df

x = open('hi.csv', encoding = "ISO-8859-1")
df = pd.read_csv(x)
df.head()

df.drop(df.columns[3:33], axis=1, inplace=True)
df.head()