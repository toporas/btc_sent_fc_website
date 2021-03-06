import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from tweet_plgin import Tweet
import gcsfs

#db connect / local imports
from data_process.statistics_data import sentiment_topics_ui, topics_sentiments, df, sentiment_topics_data

def app():
    # daily net sentiment indicators status

    st.header('**Net sentiment indicators***')
    st.write('*on a scale between -100 and 100*')

    for i, col in enumerate(st.columns(len(sentiment_topics_ui))):
        sent_today = topics_sentiments[i][0]
        diff = round(
            abs(topics_sentiments[i][0]) - abs(topics_sentiments[i][1]), 2)
        col.metric(sentiment_topics_ui[i], str(sent_today), str(diff))

    # most common words across the topics

    st.header('**Most common keywords* of the day**')
    st.write('**across all the topics listed above*')

    # dummy input - will need some sort of dictionary that has the keywords and the counts
    fs = gcsfs.GCSFileSystem()
    with fs.open('wagon-data-750-btc-sent-fc/website_data/word_text_2021_11_22.txt') as f:
        text = f.readlines()[0].decode()

    #Custom stopwords
    STOPWORDS.add('rt')
    STOPWORDS.add('will')
    STOPWORDS.add('price')
    STOPWORDS.add('now')

    # Create and generate a word cloud image:
    wordcloud = WordCloud(background_color='white', max_words=15, stopwords=None).generate_from_text(text)

    # Display the generated image:
    fig, ax = plt.subplots()

    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    st.pyplot(fig)

    # Exemplary tweets:

    st.header('**Relevant tweets**')
    t = Tweet("https://twitter.com/elonmusk/status/1454876031232380928").component()


    # historic development of net sentiment indicators

    st.header('**Historic development of net sentiment indicators**')
    st.write('Select the indicators you are interested in:')

    sentiment_topics_dict = {
        sentiment_topics_ui[i]: sentiment_topics_data[i]
        for i in range(len(sentiment_topics_ui))
    }

    for i, topic in enumerate(sentiment_topics_ui):

        if st.checkbox(sentiment_topics_ui[i], value=True):
            sentiment_topics_dict[sentiment_topics_ui[i]] = sentiment_topics_data[i]
        else:
            del sentiment_topics_dict[sentiment_topics_ui[i]]

    # test with printing dict only
    # st.write(sentiment_topics_dict)

    st.line_chart(df[list(
        sentiment_topics_dict.values())][0:30].apply(lambda x: x * 100))
