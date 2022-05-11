# twitter-tweets-counter
twitter tweets counter

# word_counter


The question which is given 

Connect to Twitter and write to Parquet / Avro file the word count of the top 100 words used every 5 minutes

Build Plan 
1. Need to connect the twitter API to get the real time data
2. check with the data need to extract what we need user, date, tweets
3. need to run with the apache spark and need to create a session
4. Or else using python fucntion we can analyse the data and finally we can convert them into the Parquet file

5. Flow affected because of essential servieces twitter can give the API access after 48 hours so for that we can go with some sample data extraction. My fav person is elon musk so for that we can get elonmusk tweets and we can analyse and perfom with the count words

for that first we need to download all the requiments
 $ pip install snscrape
 
 after that we need to import the data and use some simple pyspark model we can retreive the data and use some with column querty method we can do split or flatten the data and we can define by our self
 
 afterwards we can convert them but unfortunately i didnt use the streamin method so that i cant use time frame here sorry for that after i will get essential access i will do that also.
