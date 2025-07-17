import streamlit as st

st.title("Module 8: Best Practices & Projects")

# Day 29: Best Practices & Project Structure
st.header("Day 29: Best Practices & Project Structure")
st.write("""
Organizing your Streamlit project well makes it easier to maintain, scale, and share.
Here are some best practices:
- Use a clear folder structure (e.g., `pages/`, `data/`, `media/`, `utils/`).
- Keep secrets and config in `.streamlit/secrets.toml` and `.streamlit/config.toml`.
- Use `requirements.txt` for dependencies.
- Write modular, reusable code (use functions and separate files).
- Add a `README.md` to explain your project.
- Use version control (e.g., Git) for collaboration and backup.
""")
st.markdown("""
**Example project structure:**
```
my-streamlit-app/
│
├── app.py
├── pages/
│   ├── module1-3.py
│   └── ...
├── data/
│   └── sample.csv
├── media/
│   ├── sample_audio.mp3
│   └── sample_video.mp4
├── utils/
│   └── helpers.py
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── requirements.txt
└── README.md
```
""")
st.info("A well-structured project is easier to debug, extend, and share!")

st.markdown("---")

# Day 30: Build & Share Your Own Project
st.header("Day 30: Build & Share Your Own Project")
st.write("""
Congratulations on reaching Day 30! 🎉
Now it's time to build your own Streamlit project:
- Pick a topic or dataset you're interested in.
- Apply what you've learned: layouts, widgets, charts, uploads, downloads, and more.
- Organize your code and document your project.
- Share your app on [Streamlit Community Cloud](https://streamlit.io/cloud) or with friends and colleagues!

Thank you for joining the 30 Days of Streamlit Challenge!
""")
st.success("You did it! 🚀 Now go build something amazing.")

st.title("What Kind of Projects are Suitable for Streamlit?")

st.write("""
Streamlit is ideal for projects that require interactive data exploration, visualization, or rapid prototyping of web apps using Python. Here are some suitable project types:
""")

st.markdown("""
- **Data dashboards:** Visualize and interact with data using charts, tables, and filters.
- **Machine learning demos:** Showcase model predictions, feature importance, or interactive model tuning.
- **Data analysis tools:** Allow users to upload, clean, and analyze datasets with instant feedback.
- **Reporting apps:** Generate and share dynamic reports with visualizations and summaries.
- **Image/audio/video processing:** Build apps for tasks like image classification, audio analysis, or video previews.
- **APIs and data fetchers:** Create front-ends for querying APIs and displaying results.
- **Survey or feedback forms:** Collect and visualize user input in real time.
- **Educational tools:** Interactive tutorials, quizzes, or simulations for learning data science or programming.
""")

st.info("""
Streamlit is best for small to medium-sized apps, internal tools, prototypes, and data-driven applications where quick development and interactivity are important.
""")
st.markdown("---")  # End of Module 8