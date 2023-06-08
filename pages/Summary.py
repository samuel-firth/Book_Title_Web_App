import streamlit as st
import functions as fnc

st.title("Summary - Book Statistics")
st.write("This is a summary of your reading so far!")

st.write(f"Number of book titles in your list: {len(fnc.get_titles())}")
