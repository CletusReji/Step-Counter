import streamlit as st
import requests

# Backend API endpoint
BASE_URL = "http://127.0.0.1:5000"  # Change to your deployed backend URL if needed

# Function to register a new user
def register_user(username, password):
    response = requests.post(f"{BASE_URL}/register", json={"username": username, "password": password})
    return response.json()

# Function to authenticate login
def login_user(username, password):
    response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    return response.json()

# Streamlit UI
st.title("Step Tracker - Login & Registration")

# Select Login or Register
page = st.radio("Choose an option:", ["Login", "Register"])

if page == "Register":
    st.subheader("Create an Account")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    if st.button("Register"):
        if new_username and new_password:
            result = register_user(new_username, new_password)
            st.success(result.get("message", "Registration successful!"))
        else:
            st.warning("Please enter a username and password.")

elif page == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        result = login_user(username, password)
        if "token" in result:
            st.success("Login successful!")
            # Redirect or show the dashboard
        else:
            st.error(result.get("error", "Login failed!"))
