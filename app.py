#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt

#######################
# Page configuration

st.set_page_config(
    page_title="Futures Trading Dashboard",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# Sidebar
uploaded_file = st.sidebar.file_uploader('Upload your .csv file here:', type=['csv'])

# check if file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Session State is a way to share variables between reruns.
    st.session_state['df'] = df


#######################
# Dashboard Main Panel
col = st.columns((1.5, 4.5, 2), gap='medium')

with col[0]:
    st.markdown('#### Gains/Losses')

with col[1]:
    # Creating a Traditional Heat Map to Visualize Performance
    st.markdown('#### RORO Heat Map')

with col[2]:
    st.markdown('#### Top States')