import streamlit as st
import plotly_express as px

df = st.session_state['df']
x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
col = st.color_picker('Select a plot color')
plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
plot.update_traces(marker=dict(color=col))
st.plotly_chart(plot)