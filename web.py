import streamlit as st
import functions as fnc

titles = fnc.get_titles()


def add_title():
    title_local = st.session_state["new_title"] + "\n"
    titles.append(title_local)
    fnc.write_titles(titles)
    st.session_state["new_title"] = ""


st.title("Book Title App")
st.subheader("This app lets you track what books you have read")
st.write("Lets get reading!")
st.write("Use the checkboxes to remove titles")

for index, title in enumerate(titles):
    checkbox = st.checkbox(title, key=title,)
    if checkbox:
        titles.pop(index)
        fnc.write_titles(titles)
        del st.session_state[title]
        st.experimental_rerun()

st.text_input(label="",
              placeholder="Enter a title",
              on_change=add_title,
              key="new_title")

