import streamlit as st
from multiapp import MultiApp
import pandas as pd
import numpy as np
from apps import sentiments, forecast, methodology # import your app modules here

app = MultiApp()

url = 'https://cloudsentiment-gijujv7fiq-ew.a.run.app/'

if url == 'https://cloudsentiment-gijujv7fiq-ew.a.run.app/':
    st.markdown("""
        # **Bitcoin volume forecasting tool**
    """)

# Add all your applications here
app.add_app("💗 sentiment overview", sentiments.app)
app.add_app("🚀 bitcoin transaction volume forecast", forecast.app)
app.add_app("📚 about & methodology", methodology.app)
# The main app
app.run()
