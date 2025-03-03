import json
import os

import openai
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate


def save_key_to_session(key: str) -> None:
    """Save the OpenAI key in Streamlit session state."""
    st.session_state["OPENAI_API_KEY"] = key
    openai.api_key = key


def load_raw_document(file_path: str) -> list[Document]:
    """Load the raw document from the file path."""
    loader = PyPDFLoader(file_path)
    return loader.load()


def split_document(documents: list[Document], chunk_size: int, chunk_overlap: int) -> list[Document]:
    """Split the document into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)


def convert_message_tuple_to_template(message_template: list[tuple]) -> str:
    assert "system" in message_template[0][0], "Incorrect format for the JSON file. The `system` key is required."

    prompt_template = ChatPromptTemplate.from_messages(message_template)
    return prompt_template
