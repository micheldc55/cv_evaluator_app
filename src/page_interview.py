import streamlit as st
from src.constants import APPROVED, PDF_HEIGHT, PDF_WIDTH, REJECTED, SKIPPED, STATUS_COLOR_MAPPING
from src.dataclasses.app_dataclasses import InterviewQuestion
from src.file_management.file_management import (
    get_all_candidates_for_first_interview,
    get_candidate_filename,
    load_interview_questions,
    load_metadata,
    save_interview_questions,
    save_metadata,
)
from src.streamlit.streamlit_utils import add_n_whitespaces, display_pdf, write_status_in_colors


def interview_page():
    st.title("Interview")
    candidate_list = get_all_candidates_for_first_interview()

    if not candidate_list:
        st.info(
            "No candidates available for the first interview yet. Approve candidates from the initial screening (Evaluate Candidate page) first so they move to the first interview."
        )
    else:
        selected_candidate = st.selectbox("Select a Candidate (by ID)", candidate_list)
        metadata = load_metadata(selected_candidate)

        st.write(f"**CV filename:** {metadata.filename}")
        add_n_whitespaces(1)

        write_status_in_colors(metadata.status_first_interview.upper(), STATUS_COLOR_MAPPING)
        add_n_whitespaces(2)

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
                    key=f"score_{idx}",
                )
                try:
                    iq_list.questions[idx].score = int(score_input) if score_input.strip() != "" else 0
                except ValueError:
                    st.warning("Invalid score input, please enter a number.")
                st.markdown("---")

            new_question = st.text_area("Add a new Interview Question", key="new_question", height=100)
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
