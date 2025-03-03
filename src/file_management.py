import json
import os
from io import BytesIO

from src.app_dataclasses import CandidateMetadata, InterviewQuestionList
from src.constants import APPROVED, BASE_DIR

os.makedirs(BASE_DIR, exist_ok=True)


def get_candidate_folder(candidate_id: str) -> str:
    """Return the full folder path for a given candidate."""
    return os.path.join(BASE_DIR, candidate_id)


def get_candidate_filename(metadata: CandidateMetadata) -> str:
    """Return the filename of the candidate's CV."""
    candidate_id = metadata.id
    return os.path.join(get_candidate_folder(candidate_id), "cv.pdf")


def save_cv_file(uploaded_file: BytesIO, candidate_id: str) -> str:
    """Save the uploaded PDF to the candidate's directory."""
    candidate_dir = get_candidate_folder(candidate_id)
    os.makedirs(candidate_dir, exist_ok=True)
    file_path = os.path.join(candidate_dir, "cv.pdf")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path


def load_metadata(candidate_id: str) -> CandidateMetadata:
    """Load candidate metadata from the candidate folder.
    If it doesn't exist, return default metadata."""
    candidate_dir = get_candidate_folder(candidate_id)
    meta_path = os.path.join(candidate_dir, "metadata.json")
    if os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            metadata = CandidateMetadata(**json.load(f))
    else:
        metadata = CandidateMetadata()
    return metadata


def save_metadata(candidate_id: str, metadata: CandidateMetadata) -> None:
    """Save candidate metadata to the candidate folder."""
    candidate_dir = get_candidate_folder(candidate_id)
    os.makedirs(candidate_dir, exist_ok=True)
    meta_path = os.path.join(candidate_dir, "metadata.json")
    with open(meta_path, "w") as f:
        json.dump(metadata.model_dump(), f)


def get_all_candidates() -> list[str]:
    """Return a list of candidate IDs (folder names) in the BASE_DIR."""
    return [folder for folder in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, folder))]


def get_all_candidates_for_first_interview() -> list[str]:
    """Return a list of candidate IDs (folder names) in the BASE_DIR."""
    return [
        folder
        for folder in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, folder)) and load_metadata(folder).status_initial_screening == APPROVED
    ]


def get_all_candidates_for_second_interview() -> list[str]:
    """Return a list of candidate IDs (folder names) in the BASE_DIR."""
    return [
        folder
        for folder in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, folder)) and load_metadata(folder).status_first_interview == APPROVED
    ]


def load_interview_questions(candidate_id: str) -> InterviewQuestionList:
    """
    Load interview questions for a candidate from a JSON file.
    Returns an InterviewQuestionList. If the file doesn't exist, returns an empty list.
    """
    candidate_dir = get_candidate_folder(candidate_id)
    filepath = os.path.join(candidate_dir, "interview_questions.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
        return InterviewQuestionList.model_validate(data)
    else:
        return InterviewQuestionList(questions=[], global_feedback="")


def save_interview_questions(candidate_id: str, iq_list: InterviewQuestionList):
    """
    Save the InterviewQuestionList data to a JSON file in the candidate folder.
    """
    candidate_dir = get_candidate_folder(candidate_id)
    os.makedirs(candidate_dir, exist_ok=True)
    filepath = os.path.join(candidate_dir, "interview_questions.json")
    with open(filepath, "w") as f:
        f.write(iq_list.json())
