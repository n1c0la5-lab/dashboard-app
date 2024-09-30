import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import numpy as np
from dateutil.relativedelta import relativedelta
from datetime import datetime
import yfinance as yf


# page config

st.set_page_config(
    page_title="Futures Trading Dashboard",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")


# Creating a Traditional Heat Map to Visualize Performance

# %% Initialization

risk_tickers = [
    'ARKK', 'SPHB', 'BTC-USD', 'XBI', 'XLK', 'SOXX', 'XLY', 'IWM', 'EEM',
    'HYG', 'USO', 'DBC', 'CPER',
    'AUDJPY=X',
]

safe_tickers = [
    'TLT', 'BIL', 'SPLV', 'XLP', 'XLU', 'XLV', 'GLD',
]


# sidebar
uploaded_file = st.sidebar.file_uploader('Upload your .csv file here:', type=['csv'])


# check if file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Session State is a way to share variables between reruns.
    st.session_state['df'] = df