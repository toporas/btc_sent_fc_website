import streamlit as st
import pandas as pd

from datetime import timedelta
import requests
from data_process.statistics_data import df

# request tomorrow prediction from api
response = requests.get("https://cloudsentiment-gijujv7fiq-ew.a.run.app/predict/")


def app():

    # get last day volume from google cloud db
    yesterday = float(df['volume_gross'][0])
    today = float(response.json()['prediction'])
    #delta_yesterday =
    delta_today = today - yesterday

    st.header('**Model prediction***')
    st.write('*in USD million*')
    col1, col2 = st.columns(2)
    col1.metric("Yesterday (actual)", round(yesterday/1_000_000, 2))
    col2.metric("Today (prediction)", round(today / 1_000_000, 2),
                round(delta_today / 1_000_000, 2))

    st.header('**Prediction and recent actuals**')
    # here we need char_data to be a data frame which has two columns, actual and prediction.
    # we will fill actual for the first 29 days and put a zero in the predction column for the first 29 days
    # for the 30th day (our prediction day) we will put a zero in actual and the model prediction in prediction
    last_vol_days= df['volume_gross'][0:29]
    pred_date =pd.to_datetime(last_vol_days.index[0]).date() + timedelta(days=1)
    last_vol_days.loc[str(pred_date)] = 0
    last_vol_days.sort_index(axis=0, inplace = True, ascending=False)

    act_list = last_vol_days
    pred_list = [today,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    char_dict = {'Past': act_list, 'Prediction': pred_list}
    chart_data = pd.DataFrame(char_dict)
    st.bar_chart(chart_data)
