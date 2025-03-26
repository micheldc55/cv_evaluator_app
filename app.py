import streamlit as st
from src.constants import APP_PAGES
from src.llms.llm_utils import save_key_to_session
from src.page_candidates_overview import overview_page
from src.page_evaluate_candidate import evaluate_candidate_page
from src.page_intervew import interview_page
from src.page_upload_cv import upload_cv_page
from src.streamlit.streamlit_utils import add_n_whitespaces_to_obj

st.set_page_config(layout="wide")


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", APP_PAGES)

    add_n_whitespaces_to_obj(2, st.sidebar)
    save_key_to_session(st.sidebar.text_input("Enter your API key", type="password"))

    if page == "Upload CVs":
        upload_cv_page()

    elif page == "Evaluate Candidate":
        evaluate_candidate_page()

    elif page == "Interview":
        interview_page()

    elif page == "Overview":
        overview_page()


if __name__ == "__main__":
    main()
