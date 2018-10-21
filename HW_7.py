import tweepy
import time
import json
import random
import requests as req
import datetime
api_key = 

#List for new sources
news_source = ["FoxNews", "CNN", "BBCWorld", "CBSNews","NYTimes"]

#create lists to hold data
tweet_source = []
tweet_text = []
tweet_date = []
tweet_vader_score = []
tweet_neg_score = []
tweet_pos_score = []
tweet_neu_score = []

#begin looping thru news sources and requests tweets
for news_station in news_source:
    #loop thru each page to get 500 total tweets
    for x in range (5):
        tweets = api.user_timeline(news_station, page=x)
        for tweet in tweets:
            #parse tweet data into empty lists
            tweet_source.append(tweet["user"],["name"]
            tweet_text.append(tweet["text"])
            tweet_date.append(tweet["created_at"])
            
            #run sentiment analysis
            tweet_vader_analysis = analyzer.polarity_score(tweet["text"])
            #parse vader analysis
            tweet_vader_score.append(analyzer.polarity_score["compound"])
            tweet_neg_score.append(analyzer.polarity_score["neg"])
            tweet_pos_score.append(analyzer.polarity_score["pos"])
            tweet_neu_score.append(analyzer.polarity_score["neu"])

#create dataframe
tweet_df = pd.DataFrame({
    "tweet_source": tweet_source,
    "tweet_text": tweet_text,
    "tweet_date": tweet_date,
    "tweet_vader_score": tweet_vader_score,
    "tweet_pos_score": tweet_pos_score,
    "tweet_neg_score": tweet_neg_score,
    "tweet_neu_score": tweet_neu_score

})            

#convert tweet_df["date"] to a datetime object
tweet_df["tweet_date"] = pd.to_dateime(tweet_df["tweet_date"])

#sort values by date
tweet_df.sort_values("tweet_date", inplace=True)

#plot using matplotlib
plt.scatter(X,Y)
plt.scatter()
plt.scatter()
plt.scatter()
plt.scatter()
plt.scatter()
plt.scatter()
plt.title()

plt.savefig()

plt.show()

#bar chart
tweet_polarity_df = tweet_df.groupby(["tweet_source"]).mean()["tweet_vader_score"]


plt.bar(0, tweet_polarity_df[""])
plt.bar(1, tweet_polarity_df[""])
plt.bar(2, tweet_polarity_df[""])
plt.bar(3, tweet_polarity_df[""])
plt.bar(4, tweet_polarity_df[""])
plt.bar(5, tweet_polarity_df[""])
















