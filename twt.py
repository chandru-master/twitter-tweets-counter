import snscrape.modules.twitter as sntwitter
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import csv
import json
import requests
import numpy as np

query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"


tweets = []
limit = 4000
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content])

df = pd.DataFrame(tweets, columns=['Date','User','Tweet'])
print(df)

df = pd.DataFrame(data, columns=columns)
df.to_("tweet.csv")

