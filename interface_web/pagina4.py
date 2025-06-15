import streamlit as st

# Simulated view counter (in real use, store this in a database or file)
if 'view_count' not in st.session_state:
    st.session_state.view_count = 0
    st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
    st.subheader("This is a subheader with a divider", divider="gray")
    st.subheader("These subheaders have rotating dividers", divider=True)
    st.subheader("One", divider=True)
    st.subheader("Two", divider=True)
    st.subheader("Three", divider=True)
    st.subheader("Four", divider=True)


if st.button("Play Video"):
    st.session_state.view_count += 1
    st.video("https://www.example.com/video.mp4")


st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)
st.write(f"Total Views: {st.session_state.view_count}")
