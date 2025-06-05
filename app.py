import streamlit as st
from src.constants import (
    APP_PAGES,
    PAGE_UPLOAD_CV,
    PAGE_EVALUATE_CANDIDATE,
    PAGE_INTERVIEW_1,
    PAGE_INTERVIEW_2,
    PAGE_OVERVIEW,
    PAGE_EXPORT_BASE_QUESTIONS,
    BASE_QUESTIONS
)
from src.llms.llm_utils import save_key_to_session
from src.page_candidates_overview import overview_page
from src.page_evaluate_candidate import evaluate_candidate_page
from src.page_second_interview import second_interview_page
from src.page_interview import interview_page
from src.page_upload_cv import upload_cv_page
from src.streamlit.streamlit_utils import add_n_whitespaces_to_obj
from src.page_export_questions import export_questions_page

st.set_page_config(layout="wide")


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", APP_PAGES)

    add_n_whitespaces_to_obj(2, st.sidebar)
    save_key_to_session(st.sidebar.text_input("Enter your API key", type="password"))

    if page == PAGE_UPLOAD_CV:
        upload_cv_page()

    elif page == PAGE_EVALUATE_CANDIDATE:
        evaluate_candidate_page()

    elif page == PAGE_INTERVIEW_1:
        interview_page()

    elif page == PAGE_INTERVIEW_2:
        second_interview_page()

    elif page == PAGE_OVERVIEW:
        overview_page()

    elif page == PAGE_EXPORT_BASE_QUESTIONS:
        questions_list = BASE_QUESTIONS["questions"]
        export_questions_page(questions_list)


if __name__ == "__main__":
    main()
