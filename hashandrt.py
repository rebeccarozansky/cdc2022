
import tweepy as tw
import pandas as pd
from textblob import TextBlob
import random
import matplotlib.pyplot as plt
df = pd.read_csv("data4.csv")

df = df[abs(df["sentiment"])>.2]

hashtag = []

for value,row in df.iterrows():
    hashtag.append(df["text"][value].count("#"))


df["hashtag"] = hashtag

df.to_csv("data7.csv")

#plt.scatter(hashtag, df['retweets'], alpha=0.5)
#plt.show()

