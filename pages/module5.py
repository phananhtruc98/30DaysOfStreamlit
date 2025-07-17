import streamlit as st
import time
st.title("Module 5: App Structure & State")
st.header("Day 15: Progress Bars & Status")

st.write("""
Streamlit provides simple ways to show progress and status updates in your app.
You can use `st.progress` for progress bars and `st.spinner` for loading indicators.
""")

# Progress bar example
st.subheader("Progress Bar Example")
progress_text = "Operation in progress. Please wait."
progress_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)  # Simulate a long operation
    progress_text = f"Completed {percent_complete + 1}% of the operation."
    progress_bar.progress(percent_complete + 1, text=progress_text)
st.success("Operation completed!")

# Spinner example
st.subheader("Spinner Example")
with st.spinner("Loading data..."):
    time.sleep(1)
st.info("Data loaded successfully!")

st.markdown("---")  # End of Day 15

st.header("Day 17: Using Forms")

st.write("""
Streamlit forms let you group multiple input widgets together and process them only when the user submits the form.
This is useful for collecting related inputs and reducing unnecessary reruns.
""")

with st.form("user_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Hello, {name}! You are {age} years old.")

st.info("All widgets inside the form are only processed when you click 'Submit'.")


st.title("More Streamlit Form Examples")

# Example 1: Login Form
with st.form("login_form"):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.form_submit_button("Login")
if login:
    st.success(f"Welcome, {username}!")

st.markdown("---")

# Example 2: Feedback Form
with st.form("feedback_form"):
    st.subheader("Feedback")
    rating = st.slider("Rate your experience", 1, 5, 3)
    comments = st.text_area("Additional comments")
    send = st.form_submit_button("Send Feedback")
if send:
    st.success("Thank you for your feedback!")
    st.write("Rating:", rating)
    st.write("Comments:", comments)

st.markdown("---")

# Example 3: Search Form
with st.form("search_form"):
    st.subheader("Search")
    query = st.text_input("Enter search term")
    search = st.form_submit_button("Search")
if search:
    st.info(f"Searching for: {query}")

st.markdown("---")  # End of Day 17
st.header("Day 18: Multi-Page Apps")

st.write("""
Streamlit makes it easy to build multi-page apps by placing additional Python files in a `pages` directory.
Each file in the `pages` folder becomes a separate page in your app, accessible from the sidebar.
""")

st.markdown("""
**How to create a multi-page app:**
1. Create a folder named `pages` in your project directory.
2. Add Python files (e.g., `module1-3.py`, `data_explorer.py`) to the `pages` folder.
3. Run your app with `streamlit run app.py`.
4. Use the sidebar to navigate between pages.

**Example structure:**
```
app.py
/pages
    module1-3.py
    data_explorer.py
```
""")

st.info("Try adding new Python files to your `pages` folder and see them appear in the sidebar!")
# data/ — Store datasets or CSV files.
# images/ — Store images used in your app.
# components/ — Custom Streamlit components or reusable modules.
# utils/ — Utility functions or helper scripts.
# assets/ — Static files like CSS, JS, or icons.
# notebooks/ — Jupyter notebooks for data exploration.

st.markdown("---")  # End of Day 18

st.header("Day 19: Customizing Themes")

st.write("""
Streamlit allows you to customize the look and feel of your app using themes.
You can change colors, fonts, and other style elements by editing the `.streamlit/config.toml` file in your project directory.
""")

st.markdown("""
**How to customize your Streamlit theme:**

1. Create a folder named `.streamlit` in your project directory (if it doesn't exist).
2. Inside `.streamlit`, create a file named `config.toml`.
3. Add theme settings to `config.toml`. For example:
```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```
4. Save the file and rerun your app to see the changes.

You can also switch between "light" and "dark" modes in the app settings menu.
""")

st.info("Try editing `.streamlit/config.toml` to see your app's appearance change!")
