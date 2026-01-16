import os
import streamlit as st
import httpx

# Get backend URL from environment or default
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.title("Alpha Kabu AI")
st.write("Welcome to the Alpha Kabu AI interface.")

st.header("Backend Connection Test")
if st.button("Ping Backend"):
    try:
        response = httpx.get(f"{BACKEND_URL}/")
        if response.status_code == 200:
            st.success(f"Response from backend: {response.json()}")
        else:
            st.error(f"Failed to connect. Status: {response.status_code}")
    except httpx.RequestError as e:
        st.error(f"Connection error: {e}")

