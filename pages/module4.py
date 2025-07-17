import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
import time
st.title("Module 4: Visualization")
st.header("Day 11: Plotting with Matplotlib")

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

# Create a matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")
ax.plot(x, y2, label="cos(x)", linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("Value")
ax.set_title("Sine and Cosine Waves")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

st.header("Day 11: Realistic Example - Monthly Sales Data")
# Example data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
product_a_sales = [120, 135, 150, 170, 160, 180, 200, 210, 190, 220, 230, 250]
product_b_sales = [100, 115, 130, 140, 150, 160, 170, 180, 175, 190, 200, 210]
# Matplotlib supports many different marker styles! Here are some commonly used markers:

# 'o' : Circle
# 's' : Square
# '^' : Triangle up
# 'v' : Triangle down
# 'D' : Diamond
# 'x' : X
# '+' : Plus
# '*' : Star
# '.' : Point
# 'p' : Pentagon
# 'h' : Hexagon
# Create a matplotlib figure
fig, ax = plt.subplots()
ax.plot(months, product_a_sales, marker='x', label="Product A")
ax.plot(months, product_b_sales, marker='o', label="Product B")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales Data (Product A vs Product B)")
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("---")  # End of Day 11

st.header("Day 12: Plotting with Altair")

# Example data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
product_a_sales = [120, 135, 150, 170, 160, 180, 200, 210, 190, 220, 230, 250]
product_b_sales = [100, 115, 130, 140, 150, 160, 170, 180, 175, 190, 200, 210]

# Prepare data for Altair
df = pd.DataFrame({
    "Month": months * 2,
    "Sales": product_a_sales + product_b_sales,
    "Product": ["A"] * 12 + ["B"] * 12
})

# Create Altair chart
chart = alt.Chart(df).mark_line(point=True).encode(
    x="Month",
    y="Sales",
    color="Product",
    tooltip=["Month", "Product", "Sales"]
).properties(
    title="Monthly Sales Data (Product A vs Product B)"
)

st.altair_chart(chart, use_container_width=True)

st.markdown("---")  # End of Day 12

st.title("Module 4: Visualization")
st.header("Day 13: Caching with @st.cache_data")

st.write("""
Streamlit's `@st.cache_data` decorator helps speed up your app by caching the results of expensive computations or data loading.
When you use this decorator, Streamlit stores the function's output and reuses it if the inputs haven't changed.
""")

# Example: Simulate expensive data loading
@st.cache_data
def load_data(rows=1000):
    st.write("Loading data... (this should appear only once unless you change the input)")
    return pd.DataFrame({
        "A": np.random.randn(rows),
        "B": np.random.rand(rows)
    })

num_rows = st.slider("Number of rows to load", 100, 5000, 1000, step=100)
df = load_data(num_rows)
st.dataframe(df.head())

st.info("Change the slider to see the function rerun. If you keep the same value, the cached result is used!")

# Another example: Caching data from a CSV file
st.subheader("Example: Caching CSV file loading")

@st.cache_data
def load_csv(url):
    st.write("Reading CSV from URL... (this should appear only once per URL)")
    return pd.read_csv(url)

csv_url = st.text_input("Enter a CSV URL to load", "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
if csv_url:
    csv_df = load_csv(csv_url)
    st.dataframe(csv_df.head())

st.info("Change the URL to reload. If you keep the same URL, the cached result is used!")

# Example: Caching a slow computation
st.subheader("Example: Caching a slow computation")


@st.cache_data
def slow_square(x):
    st.write(f"Computing square of {x} (this should appear only once per value)...")
    time.sleep(2)  # Simulate a slow computation
    return x * x

number = st.number_input("Enter a number to square", 1, 100, 10)
result = slow_square(number)
st.write(f"Square of {number} is {result}")

st.markdown("---")  # End of Day 13

st.header("Day 14: Maps & Geospatial")

st.write("""
Streamlit supports simple map visualizations out of the box using `st.map`.
You can display points on a map by providing a DataFrame with latitude and longitude columns.
""")

# Generate random geospatial data (e.g., points around a city center)
num_points = st.slider("Number of points", 10, 200, 50)
city_center = [10.7769, 106.7009]  # Ho Chi Minh City, Vietnam

map_data = pd.DataFrame({
    "lat": np.random.normal(city_center[0], 0.01, num_points),
    "lon": np.random.normal(city_center[1], 0.01, num_points)
})

st.map(map_data)

st.info("You can use your own latitude/longitude data for custom maps!")

st.markdown("---")  # End of Day 14