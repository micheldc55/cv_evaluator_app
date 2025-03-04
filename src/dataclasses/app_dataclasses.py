from typing import Any

from pydantic import BaseModel

from src.constants import PENDING, APPROVED


class CandidateMetadata(BaseModel):
    id: str
    name: str = ""
    surname: str = ""
    comments: str = ""
    llm_summary_candidate: str = ""
    llm_fit_report_candidate: str = ""
    status_initial_screening: str = APPROVED
    status_first_interview: str = PENDING
    status_second_interview: str = PENDING
    filename: str = ""


class CandidateFactory:
    def create_candidate(self, candidate_params: dict[str, Any]):
        if "id" not in candidate_params:
            raise ValueError("The `id` parameter is required when creating a candidate.")

        return CandidateMetadata(**candidate_params)


class InterviewQuestion(BaseModel):
    question: str
    answer: str = ""
    score: int = 0
    feedback: str = ""


class InterviewQuestionList(BaseModel):
    questions: list[InterviewQuestion]
    global_feedback: str = ""
