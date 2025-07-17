import streamlit as st
st.title("Module 5: App Structure & State")
st.header("Day 16: Session State")

st.write("""
Streamlit's session state lets you store and persist variables across reruns, enabling more advanced app logic and user experiences.
""")

# Example: Simple counter using session state
if "counter" not in st.session_state:
    st.session_state.counter = 0

col1, col2 = st.columns(2)
increment = col1.button("Increment", key="inc_btn")
reset = col2.button("Reset", key="reset_btn")

if increment:
    st.session_state.counter += 1
if reset:
    st.session_state.counter = 0

st.write(f"Counter value: {st.session_state.counter}")
st.info("Try clicking the buttons above. The counter value will persist across reruns!")

st.markdown("---")  # End of Day 16