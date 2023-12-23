import streamlit as st
from projects import display_profile, display_project
from resume1 import resume
PAGE_TITLE = "Digital CV | Justin Borneo"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Resume", "Project"])

    if page == "Resume":
        resume()
    elif page == "Project":
        display_project()

if __name__ == "__main__":
    main()
