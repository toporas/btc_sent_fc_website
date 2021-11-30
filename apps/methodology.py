import streamlit as st
import pandas as pd
import numpy as np

def app():

    st.markdown("""
        ## Model output (y variable)
        - Bitcoin trading gross volume

        ## Model inputs (X variables)

        Scraped data:
        - Reddit posts
        - Twitter tweets

        Blockchain.com sourced KPIs:
        - N-transactions-per-block
        - Difficulty
        - Utxo-count
        - Mvrv
        - Nvt
        - Avg-block-size
        - N-transactions-excluding-popular
        - N-unique-addresses
        - Median-confirmation-time
        - Miners-revenue
        - Mempool-growth
        - Mempool-size
        - Blocks-size
        - Hash-rate
        - N-transactions-total
        - Avg-confirmation-time
        - Nvts
        - Transaction-fees-usd
        - active_account

        Financial KPIs:
        - Russell 2000 Index (RUT) - Index Value
        - CBOE Volatility S&P 500 Index (^VIX) - Index Value
        - S&P 500 (^SPX) - Index Value
        - NASDAQ Composite Index (^COMP) - Index Value
        - Dow Jones Industrial Average (^DJI) - Index Value, News Sentiment
        - S&P U.S. Treasury Bill 0-3 Month Index
        - S&P U.S. Treasury Bond 10+ Year Index
        - S&P U.S. TIPS 5+ Year Index (USD)
        - S&P U.S. Treasury Bond 1-3 Year Index
        - S&P Canada Treasury Bill Index
        - S&P U.S. Treasury Bond Current 30-Year Index
        - S&P U.S. Treasury Bond Current 5-Year Index
        - S&P Short Term Taxable Municipal Bond Index
        - S&P Taxable Municipal Bond Index
        - S&P U.S. Treasury Bond Current 2-Year Index
        - S&P U.S. Treasury Bond 7-10 Year Index
        - S&P U.S. TIPS 0-1 Year Index (USD)
        - S&P U.S. Treasury Bond 20+ Year Index
        - S&P U.S. Government & Corporate AAA-AA 1+ Year Bond Index
        - S&P Municipal Yield Index
        - S&P U.S. Treasury Bond Current 7-Year Index
        - S&P U.S. Treasury Bond Current 10-Year Index
        - S&P U.S. Treasury Bill 9-12 Month Index
        - S&P U.S. Treasury Bond Current 3-Year Index
        - S&P U.S. TIPS 30 Year Index (USD)
        - S&P U.S. Ultra Short Treasury Bill & Bond Index (USD)
        - S&P U.S. TIPS 15+ Year Index (USD)
        - S&P U.S. Treasury Bond 5-7 Year Index
        - S&P U.S. TIPS 10+ Year Index (USD)
        - S&P U.S. Treasury Bill 3-6 Month Index
        - S&P U.S. Treasury Bond 7-10 Year Index (TTM JPY)
        - S&P U.S. TIPS 7-10 Year Index (USD)
        - S&P U.S. Treasury Bond 3-5 Year Index
        - S&P U.S. TIPS 3-5 Year Index (USD)
        - S&P U.S. TIPS 1-3 Year Index (USD)
        - S&P U.S. TIPS 5-7 Year Index (USD)
        - S&P U.S. Treasury Bill 6-9 Month Index


    """)

    st.markdown("""
        ## Project methodology

        - Input 1
        - Input 1
        - Input 1

    """)
