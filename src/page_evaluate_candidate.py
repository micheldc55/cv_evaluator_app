from langchain.chains import load_summarize_chain
from langchain_community.chat_models import ChatOpenAI

import streamlit as st
from src.constants import APPROVED, BASE_QUESTIONS, REJECTED, SKIPPED, STRICTNESS_LEVELS
from src.file_management.file_management import (
    get_all_candidates,
    get_candidate_filename,
    load_metadata,
    read_dict_into_iq_list,
    save_interview_questions,
    save_metadata,
)
from src.llms.configs.llm_message_templates import FIT_REPORT_TEMPLATE
from src.llms.llm_utils import convert_message_tuple_to_template, load_raw_document
from src.streamlit.streamlit_utils import add_n_whitespaces, display_pdf, pdf_viewer_setup


def evaluate_candidate_page():
    st.title("Evaluate Candidate")
    candidate_list = get_all_candidates()

    if not candidate_list:
        st.info("No candidates available. Please upload CVs first.")

    else:
        selected_candidate = st.selectbox("Select a Candidate (by ID)", candidate_list)
        metadata = load_metadata(selected_candidate)

        _ = st.write(f"**CV filename:** {metadata.filename}")
        add_n_whitespaces(1)

        name = st.text_input("Name", value=metadata.name)
        surname = st.text_input("Surname", value=metadata.surname)
        comments = st.text_area("Comments", value=metadata.comments)

        candidate_file_path = get_candidate_filename(metadata)

        width, height = pdf_viewer_setup()

        add_n_whitespaces(1)
        display_pdf(candidate_file_path, width=width, height=height)

        st.header("Initial Screening")

        st.subheader("LLM Review:")

        st.write(
            "Below you have some options available to you in order to use LLMs to simplify the process. You can use the LLM to summarize the candidate's CV or ask questions about the CV."
        )
        st.write(
            "If you want to generate the fit report which measures the candidate's fit for the role, you need to input the job description first."
        )

        job_description = st.text_area("Job Description:")
        strictness_level = st.selectbox("Strictness Level", STRICTNESS_LEVELS)

        col1, col2, col3, _ = st.columns([1, 1, 1, 1])
        generate_summary = col1.button("Generate Summary")
        generate_fit_report = col2.button("Generate Fit Report")
        ask_questions = col3.button("Ask Questions about CV")

        if (generate_summary) and (metadata.llm_summary_candidate == ""):
            documents = load_raw_document(candidate_file_path)

            llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=st.session_state["OPENAI_API_KEY"])
            chain = load_summarize_chain(llm, chain_type="stuff", verbose=True)
            response = chain.run(documents)

            st.write(response)
            st.write(documents)

            metadata.llm_summary_candidate = response
            save_metadata(selected_candidate, metadata)
            st.success("Summary generated and saved to user metadata successfully.")

        if (generate_fit_report) and (not job_description):
            st.warning("Please input the job description first.")
        elif (generate_fit_report) and (job_description):
            documents = load_raw_document(candidate_file_path)
            llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=st.session_state["OPENAI_API_KEY"])
            messages = convert_message_tuple_to_template(FIT_REPORT_TEMPLATE)
            chain = messages | llm

            response = chain.invoke(
                {"job_description": job_description, "candidate_cv": documents, "strictness_level": strictness_level}
            )

            metadata.llm_fit_report_candidate = response.content
            save_metadata(selected_candidate, metadata)
            st.success("Fit report generated and saved to user metadata successfully.")

        if metadata.llm_fit_report_candidate:
            st.write(metadata.llm_fit_report_candidate)
        else:
            st.info("No fit report generated.")

        st.write(
            "Indicate below if the candidate should be approved or rejected to be called in for the first interview."
        )

        col1, col2, col3, _ = st.columns([1, 1, 1, 11])
        candidacy_message = None

        with col1:
            if st.button("Approve"):
                metadata.name = name
                metadata.surname = surname
                metadata.comments = comments
                metadata.status_initial_screening = APPROVED
                save_metadata(selected_candidate, metadata)

                base_questions = read_dict_into_iq_list(BASE_QUESTIONS)
                save_interview_questions(selected_candidate, base_questions)

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

                base_questions = read_dict_into_iq_list(BASE_QUESTIONS)
                save_interview_questions(selected_candidate, base_questions)

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
