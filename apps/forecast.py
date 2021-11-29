import streamlit as st
import pandas as pd
import numpy as np

def app():

    st.write('Test message to see that the page works')
    timeframe = st.radio('Select a timeframe in days', (30, 90, 180, 365))

    chart_data = pd.DataFrame(np.random.randn(timeframe, 1))
    st.bar_chart(chart_data)
