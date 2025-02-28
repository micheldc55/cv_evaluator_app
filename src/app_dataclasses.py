from pydantic import BaseModel

from src.constants import PENDING, APPROVED


class CandidateMetadata(BaseModel):
    id: str
    name: str = ""
    surname: str = ""
    comments: str = ""
    status_initial_screening: str = APPROVED
    status_first_interview: str = PENDING
    status_second_interview: str = PENDING
    filename: str = ""


class InterviewQuestion(BaseModel):
    question: str
    answer: str = ""
    score: int = 0
    feedback: str = ""


class InterviewQuestionList(BaseModel):
    questions: list[InterviewQuestion]
    global_feedback: str = ""
