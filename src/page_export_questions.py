import json

import streamlit as st

from src.streamlit.streamlit_utils import add_n_whitespaces
from src.file_management.file_management import read_and_format_json_to_text


def export_questions_page(base_question_list: list):
    st.header("Review Questions and Export them to text format")

    st.subheader("Export Questions")
    add_n_whitespaces(1)
    button = st.button("Export Questions")
    add_n_whitespaces(1)
    add_path = st.checkbox("Add specific file path")

    if add_path:
        add_n_whitespaces(1)
        file_path = st.text_input("Input Path including name! (absolute path preferred)")
        if not file_path.strip():  #check if path empty or just space
            file_path = "data/questions.txt"
    else:
        file_path = "data/questions.txt"

    if button:

        with open(file_path, "w") as f:
            questions_string = read_and_format_json_to_text(base_question_list)
            f.write(questions_string)

        st.success(f"Questions written to: `{file_path}` !!")

    st.header("Summary of Questions:")

    col1, _ = st.columns([4, 1])

    for idx, question in enumerate(base_question_list, 1):
        question_text = question["question"]
        col1.write(f"**Question {idx}:** {question_text}")

        col1.write("---")
