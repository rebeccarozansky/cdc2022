import pandas as pd
import requests, json
import csv
from textblob import TextBlob

api_key = "3af313365da13c96b5e0308f2ddbd458"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

df2 = pd.read_csv("https://raw.githubusercontent.com/rebeccarozansky/cdc2022/main/test.csv",index_col=0)
df3 = pd.DataFrame(columns=df2.columns.tolist()[1:] + ['temperature','sentiment'])

for value, row in df2.iterrows():
    city_name = df2['city'][value]
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        sent = TextBlob(df2['text'][value]).sentiment.polarity
        data = {"text": df2['text'][value], "tweet_id":df2['tweet_id'][value], "city":df2['city'][value], "country": df2['country'][value], "temperature":current_temperature, "sentiment": sent}
        df3 = df3.append(data, ignore_index=True)
    else:
        print(" City Not Found ")
