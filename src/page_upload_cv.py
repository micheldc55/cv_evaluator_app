import uuid

import streamlit as st

from src.file_management.file_management import save_cv_file, save_metadata, get_all_candidates_metadata, save_interview_questions
from src.dataclasses.app_dataclasses import CandidateFactory, InterviewQuestionList
from src.constants import PENDING, BASE_QUESTIONS


def upload_cv_page():
    st.title("Upload CVs")
    st.write("Upload one or multiple PDF CV files. Each will be saved with a unique ID.")

    uploaded_files = st.file_uploader("Choose PDF file(s)", type=["pdf"], accept_multiple_files=True)

    submit_files = st.button("Submit")

    if submit_files and uploaded_files:
        candidates_filenames = get_all_candidates_metadata("filename")

        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name

            if file_name in candidates_filenames:
                st.warning(f"File {file_name} already exists!")

            else:
                candidate_id = str(uuid.uuid4())
                save_cv_file(uploaded_file, candidate_id)

                default_metadata = CandidateFactory.create_candidate(
                    candidate_params={
                        "id": candidate_id,
                        "status_initial_screening": PENDING,
                        "status_first_interview": PENDING,
                        "status_second_interview": PENDING,
                        "filename": uploaded_file.name,

                    }
                )
                save_metadata(candidate_id, default_metadata)

                default_interview_questions = InterviewQuestionList(**BASE_QUESTIONS)
                save_interview_questions(candidate_id, default_interview_questions)
                
                st.success(f"Uploaded and saved CV for candidate ID: {candidate_id}")
            
    elif submit_files and not uploaded_files:
        st.warning("Please upload at least one PDF file.")
