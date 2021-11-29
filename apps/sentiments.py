import streamlit as st
import pandas as pd
import numpy as np

def app():

    # daily net sentiment indicators status

    st.header('**Net sentiment indicators***')
    st.write('*on a scale between -100 and 100*')
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Bitcoin", "50.0", "-10.25")
    col2.metric("Economy", "50.0", "-10.25")
    col3.metric("Inflation", "50.0", "-10.25")
    col4.metric("Econ topic #3", "50.0", "-10.25")
    col5.metric("Econ topic #4", "50.0", "-10.25")

    # historic development of net sentiment indicators

    st.header('**Historic development of net sentiment indicators**')

    st.write('Select the indicators you are interested in:')
    option_1 = st.checkbox("Bitcoin")
    option_2 = st.checkbox("Economy")
    option_3 = st.checkbox("Inflation")
    option_4 = st.checkbox("Econ topic #3")
    option_5 = st.checkbox("Econ topic #4")
    # IMPORTANT - still need to connect the checkboxes with the chart

    chart_data = pd.DataFrame(np.random.randn(20, 5),columns=["Bitcoin", "Economy", "Inflation", "Econ topic #3", "Econ topic #4"])

    st.area_chart(chart_data)
