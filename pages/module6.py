import streamlit as st
import pandas as pd
import time
from st_aggrid import AgGrid, GridOptionsBuilder
from streamlit_tags import st_tags
import numpy as np

st.title("Module 6: Advanced Features")
st.header("Day 20: Caching - Real World Example")

st.write("""
Suppose you have a large CSV file. Loading it every time is slow.
With `@st.cache_data`, you only load it once unless the file path changes.
""")

@st.cache_data
def load_data(csv_path):
    st.write("Loading data from CSV...")
    time.sleep(2)  # Simulate slow file loading
    return pd.read_csv(csv_path)

# For demonstration, use a sample CSV from the web
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
st.write(f"Loading data from: {csv_url}")

df = load_data(csv_url)
st.dataframe(df.head())

st.info("Try re-running the app. The data loads instantly from cache unless the URL changes.")

st.markdown("---")  # End of Day 20

import streamlit.components.v1 as components

st.header("Day 21: Using Streamlit Components")

st.write("""
Streamlit Components let you embed custom HTML, JavaScript, or third-party widgets in your app.
You can use built-in components like `st.components.v1.html` or install community components for extra features.
""")

# Example: Embed custom HTML
st.subheader("Embed Custom HTML")
components.html(
    """
    <div style="padding:20px; background:#f0f2f6; border-radius:8px;">
        <h3 style="color:#F63366;">This is a custom HTML block!</h3>
        <p>You can use HTML and JavaScript here.</p>
    </div>
    """,
    height=120,
)

st.markdown("---")

# Example: Use a community component (if installed)
st.subheader("Community Component Example")
st.write("Try installing and using components from https://streamlit.io/components for more functionality!")

# Example: Use streamlit-aggrid (if installed)
try:
    st.write("Below is an interactive AgGrid table (requires `st-aggrid`):")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()
    gb.configure_side_bar()
    gridOptions = gb.build()
    AgGrid(df, gridOptions=gridOptions, height=200)
except ImportError:
    st.warning("Install `st-aggrid` to see an interactive grid table: `pip install streamlit-aggrid`")

# Example: Use streamlit-tags (if installed)
try:
    st.write("Below is a tag input widget (requires `streamlit-tags`):")
    tags = st_tags(
        label='Enter tags:',
        text='Press enter to add more',
        value=['Streamlit', 'Component'],
    )
    st.write("Tags:", tags)
except ImportError:
    st.warning("Install `streamlit-tags` to use the tag input widget: `pip install streamlit-tags`")

st.markdown("---")  # End of Day 21


st.header("Day 22: Animations and Lottie Files")

st.write("""
You can add simple animations to your Streamlit app using GIFs or Lottie files.
Lottie is a lightweight animation format that works well in web apps.
To use Lottie files, you need the `streamlit-lottie` package.
""")

# Show a GIF animation
st.subheader("GIF Animation Example")
st.image("https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif", caption="Celebration GIF", use_column_width=True)

st.markdown("---")

# Show a Lottie animation (if streamlit-lottie is installed)
try:
    from streamlit_lottie import st_lottie
    import requests

    st.subheader("Lottie Animation Example")
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=200)
    else:
        st.warning("Could not load Lottie animation.")
except ImportError:
    st.info("Install `streamlit-lottie` to display Lottie animations: `pip install streamlit-lottie`")

st.markdown("---")  # End of Day 22

st.header("Day 23: Error Handling & Debugging")

st.write("""
Streamlit provides tools to help you handle errors and debug your app.
You can use `st.error`, `st.warning`, and `st.exception` to display error messages and exception details.
""")

# Example: Handling a division by zero error
st.subheader("Error Handling Example")
try:
    x = st.number_input("Enter a number to divide 100 by:", value=1)
    result = 100 / x
    st.success(f"100 divided by {x} is {result}")
except Exception as e:
    st.error("An error occurred!")
    st.exception(e)

st.markdown("""
**Tips for Debugging:**
- Use `st.write()` or `st.code()` to print variables and inspect data.
- Use `st.exception()` to show full tracebacks for debugging.
- Check the terminal for detailed error logs.
""")

st.markdown("---")  # End of Day 23

st.header("Day 24: Performance Optimization")

st.write("""
Optimizing your Streamlit app can make it faster and more responsive, especially with large datasets or expensive computations.
Here are some tips:
- Use `@st.cache_data` and `@st.cache_resource` to avoid redundant computations.
- Limit the amount of data loaded or displayed at once.
- Use efficient data structures and vectorized operations (e.g., with NumPy or pandas).
- Minimize reruns by grouping widgets in forms or using session state.
""")

# Example: Compare cached vs. non-cached data loading
st.subheader("Cached vs. Non-Cached Data Loading")

@st.cache_data
def load_data_cached(n):
    time.sleep(2)
    return pd.DataFrame(np.random.randn(n, 3), columns=["A", "B", "C"])

def load_data_uncached(n):
    time.sleep(2)
    return pd.DataFrame(np.random.randn(n, 3), columns=["A", "B", "C"])

rows = st.slider("Number of rows", 1000, 10000, 5000, step=1000)

col1, col2 = st.columns(2)
with col1:
    st.write("With @st.cache_data:")
    df_cached = load_data_cached(rows)
    st.dataframe(df_cached.head())
with col2:
    st.write("Without caching:")
    df_uncached = load_data_uncached(rows)
    st.dataframe(df_uncached.head())

st.info("Try changing the slider and observe the loading time difference between cached and non-cached functions.")

st.markdown("---")  # End of Day 24