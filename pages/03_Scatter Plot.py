import streamlit as st
import matplotlib.pyplot as plt

df = st.session_state['df']
# Display a plot
fig, ax = plt.subplots(1,1)
# hardcoded just for learning ..
ax.scatter(x=df['TradeQuantity'], y=df['Duration'])
# Data Visualisation
ax.set_xlabel('TradeQuantity')
ax.set_ylabel('Duration')
# Show the stuff by passing in a figure object
st.pyplot(fig)