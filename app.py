import uuid

import streamlit as st

from src.app_dataclasses import CandidateMetadata, InterviewQuestion
from src.file_management import (
    get_all_candidates, 
    get_all_candidates_for_first_interview,
    get_all_candidates_for_second_interview,
    save_cv_file, 
    save_metadata, 
    load_metadata, 
    get_candidate_filename, 
    load_interview_questions, 
    save_interview_questions
)
from src.streamlit_utils import add_n_whitespaces, display_pdf, pdf_viewer_setup
from src.constants import APP_PAGES, APPROVED, PENDING, REJECTED, SKIPPED, PDF_WIDTH, PDF_HEIGHT


st.set_page_config(layout="wide")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", APP_PAGES)

    # -----------------------------
    # Page 1: Upload CVs
    # -----------------------------
    if page == "Upload CVs":
        st.title("Upload CVs")
        st.write("Upload one or multiple PDF CV files. Each will be saved with a unique ID.")

        uploaded_files = st.file_uploader("Choose PDF file(s)", type=["pdf"], accept_multiple_files=True)
        
        submit_files = st.button("Submit")
        
        if submit_files and uploaded_files:
            for uploaded_file in uploaded_files:
                candidate_id = str(uuid.uuid4())
                save_cv_file(uploaded_file, candidate_id)
                
                default_metadata = CandidateMetadata(id=candidate_id, name="", surname="", comments="", status_initial_screening=PENDING, status_first_interview=PENDING, status_second_interview=PENDING, filename=uploaded_file.name)
                save_metadata(candidate_id, default_metadata)
                st.success(f"Uploaded and saved CV for candidate ID: {candidate_id}")
        elif submit_files and not uploaded_files:
            st.warning("Please upload at least one PDF file.")

    # -----------------------------
    # Page 2: Evaluate Candidate
    # -----------------------------
    elif page == "Evaluate Candidate":
        st.title("Evaluate Candidate")
        candidate_list = get_all_candidates()
        
        if not candidate_list:
            st.info("No candidates available. Please upload CVs first.")
        else:
            selected_candidate = st.selectbox("Select a Candidate (by ID)", candidate_list)
            metadata = load_metadata(selected_candidate)
            
            _ = st.write(f'**CV filename:** {metadata.filename}')
            add_n_whitespaces(1)

            name = st.text_input("Name", value=metadata.name)
            surname = st.text_input("Surname", value=metadata.surname)
            comments = st.text_area("Comments", value=metadata.comments)

            candidate_file_path = get_candidate_filename(metadata)

            width, height = pdf_viewer_setup()

            add_n_whitespaces(1)
            display_pdf(candidate_file_path, width=width, height=height)

            st.header("Initial Screening")
            st.write("Indicate below if the candidate should be approved or rejected to be called in for the first interview.")
            
            col1, col2, col3, _ = st.columns([1, 1, 1, 11])
            candidacy_message = None

            with col1:
                if st.button("Approve"):
                    metadata.name = name
                    metadata.surname = surname
                    metadata.comments = comments
                    metadata.status_initial_screening = APPROVED
                    save_metadata(selected_candidate, metadata)

                    candidacy_message = f"Candidate {selected_candidate} {APPROVED}."
                    
            with col2:
                if st.button("Reject"):
                    metadata.name = name
                    metadata.surname = surname
                    metadata.comments = comments
                    metadata.status_initial_screening = REJECTED
                    metadata.status_first_interview = SKIPPED
                    metadata.status_second_interview = SKIPPED
                    save_metadata(selected_candidate, metadata)

                    candidacy_message = f"Candidate {selected_candidate} {REJECTED}."
                    
            with col3:
                if st.button("Save"):
                    metadata.name = name
                    metadata.surname = surname
                    metadata.comments = comments
                    
                    save_metadata(selected_candidate, metadata)

                    candidacy_message = f"Candidate {selected_candidate} information saved."
                    
            if candidacy_message:
                st.success(candidacy_message)

    # -----------------------------
    # Page 3: Interview
    # -----------------------------
    elif page == "Interview":
        st.title("Interview")
        candidate_list = get_all_candidates_for_first_interview()

        if not candidate_list:
            st.info("No candidates available for the first interview yet. Approve candidates from the initial screening (Evaluate Candidate page) first so they move to the first interview.")
        else:
            selected_candidate = st.selectbox("Select a Candidate (by ID)", candidate_list)
            metadata = load_metadata(selected_candidate)

            st.write(f'**CV filename:** {metadata.filename}')
            add_n_whitespaces(1)

            candidate_file_path = get_candidate_filename(metadata)
            
            col1, col2 = st.columns([3, 2])
            
            with col1:
                display_pdf(candidate_file_path, width=PDF_WIDTH, height=PDF_HEIGHT)
            
            with col2:
                st.write("### Interview Questions & Feedback")
                iq_list = load_interview_questions(selected_candidate)

                for idx, iq in enumerate(iq_list.questions):
                    st.write(f"**Question {idx+1}:** {iq.question}")
            
                    feedback = st.text_area(f"Feedback for Question {idx+1}", value=iq.feedback, key=f"feedback_{idx}")
                    iq_list.questions[idx].feedback = feedback
            
                    score_input = st.text_input(
                        f"Score for Question {idx+1} (optional)",
                        value=str(iq.score) if iq.score != 0 else "",
                        key=f"score_{idx}"
                    )
                    try:
                
                        iq_list.questions[idx].score = int(score_input) if score_input.strip() != "" else 0
                    except ValueError:
                        st.warning("Invalid score input, please enter a number.")
                    st.markdown("---")

        
                new_question = st.text_input("Add a new Interview Question", key="new_question")
                if st.button("Add Question"):
                    if new_question.strip() != "":
                        iq_list.questions.append(InterviewQuestion(question=new_question))
                        save_interview_questions(selected_candidate, iq_list)
                        # st.success("Question added successfully.")
                        st.rerun()
                    else:
                        st.warning("Please enter a valid question.")

                # Global feedback for the interview
                st.subheader("Conclusions:")
                global_feedback = st.text_area("Overall Feedback", value=iq_list.global_feedback, key="global_feedback")
                iq_list.global_feedback = global_feedback

                if st.button("Save Interview Questions and Feedback"):
                    save_interview_questions(selected_candidate, iq_list)
                    st.success("Interview questions and feedback saved successfully.")

                col1, col2, _ = st.columns([1, 1, 2])

                with col1:
                    if st.button("Approve Candidate"):
                        metadata.status_first_interview = APPROVED
                        save_metadata(selected_candidate, metadata)
                        st.success("Candidate approved successfully.")
                        st.rerun()

                with col2:
                    if st.button("Reject Candidate"):
                        metadata.status_first_interview = REJECTED
                        metadata.status_second_interview = SKIPPED
                        save_metadata(selected_candidate, metadata)
                        st.success("Candidate rejected successfully.")
                
            

    # -----------------------------
    # Page 4: Overview
    # -----------------------------
    elif page == "Overview":
        st.title("Overview of Candidate Evaluations")
        candidate_list = get_all_candidates()
        
        if not candidate_list:
            st.warning("No candidates available yet.")
        else:
            overview_data = []
            for candidate_id in candidate_list:
                metadata = load_metadata(candidate_id)
                overview_data.append({
                    "Candidate ID": candidate_id,
                    "Name": metadata.name,
                    "Surname": metadata.surname,
                    "Initial Screening Status": metadata.status_initial_screening,
                    "First Interview Status": metadata.status_first_interview,
                    "Second Interview Status": metadata.status_second_interview
                })
            st.table(overview_data)


if __name__ == "__main__":
    main()
