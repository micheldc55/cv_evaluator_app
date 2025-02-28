import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

from src.constants import PDF_WIDTH, PDF_HEIGHT
def add_n_whitespaces_to_obj(n: int, obj: str) -> None:
    """Add n whitespaces to the object."""
    [obj.write("") for _ in range(n)]


def add_n_whitespaces(n: int) -> None:
    """Add n whitespaces to the object."""
    [st.write("") for _ in range(n)]


def display_pdf(pdf_path: str, width: int | None = None, height: int | None = None) -> None:
    """Preview a PDF file."""
    pdf_viewer(pdf_path, width=width, height=height)


def pdf_viewer_setup() -> tuple[int, int]:
    """Set up the PDF viewer."""
    st.subheader("Configure the size of the pdf in your screen")

    width = st.number_input("Input CV Width:", value=PDF_WIDTH)
    if not width:
        width = PDF_WIDTH
    height = st.number_input("Input CV Height:", value=PDF_HEIGHT)
    if not height:
        height = PDF_HEIGHT

    return width, height