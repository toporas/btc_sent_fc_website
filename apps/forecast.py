import streamlit as st
import pandas as pd
import numpy as np
import random

def app():

    yesterday = 2.8
    today = 4.0
    #delta_yesterday =
    delta_today = today - yesterday

    st.header('**Model prediction***')
    st.write('*in USD billion*')
    col1, col2 = st.columns(2)
    col1.metric("Yesterday (actual)", yesterday)
    col2.metric("Today (prediction)", today, round(delta_today,2))

    st.header('**Prediction and recent actuals**')
    # here we need char_data to be a data frame which has two columns, actual and prediction.
    # we will fill actual for the first 29 days and put a zero in the predction column for the first 29 days
    # for the 30th day (our prediction day) we will put a zero in actual and the model prediction in prediction
    act_list = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,0]
    pred_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,today]

    char_dict = {'Actuals': act_list, 'Prediction': pred_list}
    chart_data = pd.DataFrame(char_dict)
    st.bar_chart(chart_data)
