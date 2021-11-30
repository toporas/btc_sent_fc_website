import streamlit as st
import pandas as pd
import numpy as np

def app():

    st.header('**Mean absolute percentage error (MAPE)***')
    st.write('*selected measure of prediction accuracy, the lower the better*')
    col1, col2 = st.columns(2)
    col1.metric("Yesterday's MAPE", "5.0", "+0.25")
    col2.metric("Past 30 days MAPE", "5.0", "+0.25")

    st.header('**Actuals vs. prediction chart**')
    st.write('*Past 30 days*')
    df = pd.DataFrame(np.random.randn(30, 2),columns=['actuals', 'predictions'])

    st.line_chart(df)
