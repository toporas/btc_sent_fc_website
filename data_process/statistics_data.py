import gcsfs
import pandas as pd


# pull data from google storage
df = pd.read_csv(
    "gcs://wagon-data-750-btc-sent-fc/input_data/input_data_1.csv",
    index_col='Unnamed: 0')

# sort on date index and pull most recet 2 dates of dataframe
df = df.sort_index(
    axis=0,
    ascending=False)

#pull last today and yesterday sentiment for each topic in a dict
def get_topics_sentiment(sentiment_topics):  #get sentiment
    """ returns a list of lists with with today, yesterday sentiment values, on a scale -100 to 100 for each topic"""
    topics_list = []
    for topic in sentiment_topics:

        today_sent = round(df[topic][0] * 100, 2)
        yesterday_sent = round(df[topic][1] * 100, 2)

        topics_list.append([today_sent, yesterday_sent])
    return topics_list


################################################################################
# define a list with topics from the df (name of feature) for use in sentiments.py
################################################################################
sentiment_topics_data = ['tweets_sent','reddit_crypto_sent','reddit_econ_sent'] # make a list with topics from the df (name of feature)
sentiment_topics_ui = ['Tweeter Econ Sentiment', 'Reddit Crypto Sentiment', 'Reddit Economy Sentiment']

topics_sentiments = get_topics_sentiment(sentiment_topics_data)
################################################################################
