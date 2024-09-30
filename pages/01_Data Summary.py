import streamlit as st

df = st.session_state['df']
st.header('Data Statistics')
st.write(df.describe())