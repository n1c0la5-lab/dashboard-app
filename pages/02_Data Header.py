import streamlit as st

df = st.session_state['df']
st.header('Data Header')
st.write(df.head())