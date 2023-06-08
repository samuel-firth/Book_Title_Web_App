import streamlit as st
import functions as fnc

st.title("About")
st.write("Hello, this is all about this app")

st.write("This is just a very simple app that allows you to type in what books you have read")
st.write("I might increase the functionality over time to give it a more comprehensive utility")
st.write("<u>Ideas for Improvements:</u><br>"
         "1. Add Genre label<br>"
         "2. Add Author label<br>"
         "3. Add Book length<br>"
         "4. Add 'comment' section<br>"
         "5. Add a rating<br>"
         "6. Mark as 'read' or 'in progress'<br>"
         "7. Add start and end dates of reading<br><br>"
         "This should allow you to compile book lists of 'to-read' and 'read'",
         unsafe_allow_html=True)

titles = fnc.get_titles()

for title in titles:
    with st.expander(title):
        st.radio("Progress", options=["In progress", "Completed"], key=f"progress{title}", horizontal=True)
        st.text_input(label="Start Date", key=f"start{title}"),
        st.text_input(label="End Date", key=f"end{title}")
        st.radio("Rating", options=[1, 2, 3, 4, 5], key=f"rating{title}", horizontal=True)
        st.text_input(label="", placeholder="Genre", key=f"genre{title}")
        st.text_input(label="", placeholder="Author", key=f"author{title}")
        st.slider("Length", min_value=0, max_value=1000, key=f"length{title}")
        st.text_area(label="", placeholder="Book Summary", key=f"summary{title}")




