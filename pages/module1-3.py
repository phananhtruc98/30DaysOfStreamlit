import streamlit as st
from datetime import date
import datetime
import pandas as pd
import numpy as np

# ---------------- Module 1: Getting Started ----------------
st.title("Module 1: Getting Started")

# Day 1: Introduction & Installation
st.header("Day 1: Introduction & Installation")
st.title("Hello, Streamlit!")
st.write("Welcome to Day 1 of the 30 Days of Streamlit Challenge.")
st.markdown("---")

# Day 2: First App & Basic Elements
st.header("Day 2: First App & Basic Elements")
st.header("Welcome to Day 2!")
st.subheader("Let's explore Streamlit basics.")
st.write("Streamlit makes it easy to build web apps with Python.")
st.write("You can display text, data, charts, and more!")
st.write("2 + 2 =", 2 + 2)
st.markdown("# This is a Markdown Heading")
st.markdown("**Bold text**, *italic text*, and [a link](https://streamlit.io)")
st.markdown("""
- Bullet list
- Another item
""")
st.write("Hello, Streamlit!")
st.write("The answer is", 42)
st.write("5 * 7 =", 5 * 7)
st.write([1, 2, 3, 4, 5])
st.write({"name": "Alice", "age": 30})
st.markdown("---")

# Day 3: Text Elements
st.header("Day 3: Text Elements")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is plain text.")
st.markdown("""
**Markdown** _lets you_ format text:
- **Bold**
- *Italic*
- [Links](https://streamlit.io)
""")
st.code("""
def hello():
    print("Hello, Streamlit!")
""", language='python')
st.latex(r"""
E = mc^2
""")
st.markdown("---")

# ---------------- Module 2: Data Display ----------------
st.title("Module 2: Data Display")

# Day 4: DataFrames & Tables
st.header("Day 4: DataFrames & Tables")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85.5, 92.3, 88.7]
}
df = pd.DataFrame(data)
st.header("st.dataframe (interactive)")
st.dataframe(df)
st.header("st.table (static)")
st.table(df)
st.header("Random DataFrame Example")
random_df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)
st.dataframe(random_df)
st.markdown("---")

# ---------------- Module 3: Interactivity ----------------
st.title("Module 3: Interactivity")

# Day 5: Images, Audio, Video, File Uploads
st.header("Day 5: Images, Audio, Video, File Uploads")
st.header("Display Image")
st.image(
    "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
    caption="Streamlit Logo",
    width=300
)
st.header("Play Audio")
try:
    audio_file = open("media/sample_audio.mp3", "rb")  # Make sure this file exists
    st.audio(audio_file, format="audio/mp3")
except Exception:
    st.info("sample_audio.mp3 not found.")
st.header("Play Video")
try:
    video_file = open("media/sample_video.mp4", "rb")  # Make sure this file exists
    st.video(video_file)
except Exception:
    st.info("sample_video.mp4 not found.")
st.title("File Uploader Example")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)
    if uploaded_file.type.startswith("image"):
        st.image(uploaded_file)
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    else:
        st.write("File type:", uploaded_file.type)
st.title("Multiple File Upload Example")
uploaded_files = st.file_uploader(
    "Choose files",
    accept_multiple_files=True
)
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write("Filename:", uploaded_file.name)
        if uploaded_file.type.startswith("image"):
            st.image(uploaded_file)
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
        else:
            st.write("File type:", uploaded_file.type)
st.markdown("---")

# Day 6: Button and Checkbox
st.header("Day 6: Button and Checkbox")
if st.button("Click Me!"):
    st.success("Button was clicked!")
show_text = st.checkbox("Show secret message")
if show_text:
    st.info("🎉 You found the secret message!")
if st.checkbox("Enable feature") and st.button("Another Button"):
    st.write("Both the button and checkbox are active!")
st.success("Operation completed successfully!")
st.warning("This is a warning message.")
st.error("An error has occurred.")
st.info("This is some information.")
try:
    1 / 0
except Exception as e:
    st.exception(e)
st.markdown("---")

# Day 7: Sliders & Selectboxes
st.header("Day 7: Sliders & Selectboxes")
st.title("Slider Examples")
age = st.slider("Select your age", min_value=0, max_value=100, value=25)
st.write("Your age is:", age)
int_value = st.slider("Pick an integer", 0, 100, 50)
st.write("Integer value:", int_value)
float_value = st.slider("Pick a float", 0.0, 1.0, 0.5, step=0.01)
st.write("Float value:", float_value)
range_int = st.slider("Pick a range of integers", 0, 100, (20, 80))
st.write("Integer range:", range_int)
range_float = st.slider("Pick a range of floats", 0.0, 10.0, (2.5, 7.5), step=0.1)
st.write("Float range:", range_float)
level = st.slider("Select difficulty", 1, 5, 3, format="Level %d")
st.write("Selected level:", level)
start_time = st.slider(
    "Select a time",
    min_value=datetime.time(8, 0),
    max_value=datetime.time(18, 0),
    value=datetime.time(12, 0),
    step=datetime.timedelta(minutes=15)
)
st.write("Selected time:", start_time)
color = st.selectbox(
    "Pick a color",
    options=["Red", "Green", "Blue", "Yellow"]
)
st.write("You selected:", color)
if color == "Red":
    st.error("Red selected!")
elif color == "Green":
    st.success("Green selected!")
else:
    st.info(f"{color} selected!")
st.markdown("---")

# Day 8: Text, Number, Date Inputs
st.header("Day 8: Text, Number, Date Inputs")
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
st.write(f"Your age is: {age}")
birthday = st.date_input("Select your birthday", value=date(2000, 1, 1))
st.write(f"Your birthday is: {birthday}")
st.markdown("---")

# Day 9: Layouts (Columns, Expander, Sidebar)
st.header("Day 9: Layouts (Columns, Expander, Sidebar)")
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the left column.")
with col2:
    st.header("Column 2")
    st.write("This is the right column.")
with st.expander("See more details"):
    st.write("Here you can put additional information that is hidden by default.")
st.sidebar.title("Sidebar Example")
sidebar_option = st.sidebar.selectbox(
    "Choose an option",
    ["Option 1", "Option 2", "Option 3"]
)
st.sidebar.write(f"You selected: {sidebar_option}")
st.sidebar.title("Sidebar Controls")
username = st.sidebar.text_input("Username")
if username:
    st.sidebar.write(f"Hello, {username}!")
rating = st.sidebar.slider("Rate our app", 1, 5, 3)
st.sidebar.write(f"Your rating: {rating}")
color = st.sidebar.selectbox("Favorite color", ["Red", "Green", "Blue"])
st.sidebar.write(f"Selected color: {color}")
show_info = st.sidebar.checkbox("Show info")
if show_info:
    st.sidebar.info("Here is some extra information in the sidebar.")
if st.sidebar.button("Click me!"):
    st.sidebar.success("Button clicked in the sidebar!")
uploaded = st.sidebar.file_uploader("Upload a file")
if uploaded:
    st.sidebar.write("File uploaded:", uploaded.name)
st.markdown("---")