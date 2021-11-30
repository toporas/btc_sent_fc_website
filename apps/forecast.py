import streamlit as st
import pandas as pd
import numpy as np

def app():

    yesterday = 2.8
    today = 4.0
    tomorrow = 5.0
    #delta_yesterday =
    delta_today = today - yesterday
    delta_tomorrow = tomorrow - today

    st.header('**Model predictions***')
    st.write('*in USD billion*')
    col1, col2, col3 = st.columns(3)
    col1.metric("Yesterday (actual)", yesterday)
    col2.metric("Today (prediction)", today, round(delta_today,2))
    col3.metric("Tomorrow (prediction)", tomorrow, round(delta_tomorrow,2))

    timeframe = st.radio('Select a timeframe in days', (30, 90, 180, 365))

    chart_data = pd.DataFrame(np.random.randn(timeframe, 1))
    st.bar_chart(chart_data)
