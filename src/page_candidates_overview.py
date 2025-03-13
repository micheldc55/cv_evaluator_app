import streamlit as st
from src.file_management.file_management import get_all_candidates, load_metadata


def overview_page():
    st.title("Overview of Candidate Evaluations")
    candidate_list = get_all_candidates()

    if not candidate_list:
        st.warning("No candidates available yet.")
    else:
        overview_data = []
        for candidate_id in candidate_list:
            metadata = load_metadata(candidate_id)
            overview_data.append(
                {
                    "Candidate ID": candidate_id,
                    "Name": metadata.name,
                    "Surname": metadata.surname,
                    "Initial Screening Status": metadata.status_initial_screening,
                    "First Interview Status": metadata.status_first_interview,
                    "Second Interview Status": metadata.status_second_interview,
                }
            )
        st.table(overview_data)
