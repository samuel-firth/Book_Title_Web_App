import streamlit as st

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
