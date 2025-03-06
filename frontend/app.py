import streamlit as st
import pandas as pd
import requests

st.title("Daily Step Tracker")

# Fetch data from API
response = requests.get("http://localhost:5000/get_data")
df = pd.DataFrame(response.json())

st.write("### Step Count Data")
st.dataframe(df)

st.write("### Step Count Trends")
st.line_chart(df.set_index("date")["steps"])