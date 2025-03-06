import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.title("Daily Step Tracker")

# User Authentication
if "username" not in st.session_state:
    st.session_state.username = None

# Login Form
if st.session_state.username is None:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
        if response.status_code == 200:
            st.session_state.username = response.json()["username"]
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# If logged in, show step tracking features
if st.session_state.username:
    st.subheader("Track Your Steps")

    # Step Input
    date = st.date_input("Select Date")
    steps = st.number_input("Enter Steps", min_value=0, step=1)

    if st.button("Add Step Data"):
        response = requests.post(f"{BASE_URL}/add_step", json={"username": st.session_state.username, "date": str(date), "steps": steps})
        if response.status_code == 201:
            st.success("Step data added successfully!")
        else:
            st.error("Error adding step data")

    # Show Step Data
    st.subheader("Your Step History")
    response = requests.get(f"{BASE_URL}/get_steps/{st.session_state.username}")
    if response.status_code == 200:
        step_data = response.json()
        for record in step_data:
            st.write(f"📅 {record['date']} - 🚶 {record['steps']} steps")
    else:
        st.write("No step data available")