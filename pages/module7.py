import streamlit as st
import requests
import pandas as pd

st.title("Module 7: Integration & Deployment")

# Day 25: API Integration
st.header("Day 25: API Integration")
st.write("""
You can fetch and display data from APIs in Streamlit using Python's `requests` library.
Below is an example that fetches random user data from a public API.
""")
if st.button("Fetch Random User"):
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        user = response.json()["results"][0]
        st.write("Name:", user["name"]["first"], user["name"]["last"])
        st.write("Email:", user["email"])
        st.image(user["picture"]["large"])
    else:
        st.error("Failed to fetch data from API.")
st.markdown("---")

# Day 26: Authentication Basics
st.header("Day 26: Authentication Basics")
st.write("""
For production apps, use secure authentication solutions.
For demonstration, here's a simple username/password check.
""")
with st.form("auth_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.form_submit_button("Login")
if login:
    if username == "user" and password == "streamlit":
        st.success("Login successful!")
    else:
        st.error("Invalid credentials.")
st.markdown("---")

# Day 27: File Downloads
st.header("Day 27: File Downloads")
st.write("""
You can let users download data or files using `st.download_button`.
""")
sample_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.download_button(
    label="Download sample CSV",
    data=sample_df.to_csv(index=False),
    file_name="sample.csv",
    mime="text/csv"
)
st.markdown("---")

# Day 28: Deploying to Streamlit Cloud
st.header("Day 28: Deploying to Streamlit Cloud")
st.write("""
You can deploy your Streamlit app for free using [Streamlit Community Cloud](https://streamlit.io/cloud).
1. Push your code to a public GitHub repository.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your repo.
3. Click 'Deploy' and your app will be live!
""")
st.info("Check the [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud) for more details.")

st.markdown("---")  # End of Module 7
