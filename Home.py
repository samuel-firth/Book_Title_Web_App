import streamlit as st
import functions as fnc

titles = fnc.get_titles()
st.set_page_config(layout="wide")


def add_title():
    title_local = st.session_state["new_title"] + "\n"
    titles.append(title_local)
    fnc.write_titles(titles)
    st.session_state["new_title"] = ""


st.title("Book Title App - Home")
st.subheader("This app lets you track what books you have read")
st.write("Lets get reading! - You can always use the checkboxes to <b>delete a title if needed!</b>",
         unsafe_allow_html=True)

st.text_input(label="",
              placeholder="Enter a title",
              on_change=add_title,
              key="new_title")

for index, title in enumerate(titles):
    checkbox = st.checkbox(title, key=title,)
    if checkbox:
        titles.pop(index)
        fnc.write_titles(titles)
        del st.session_state[title]
        st.experimental_rerun()



