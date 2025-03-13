FIT_REPORT_TEMPLATE = [
    (
        "system",
        "You are a helpful assistant that is given a job description, a candidate's CV and how strict the screening process is. You are tasked with generating a short fit report for the candidate based on the job description.",
    ),
    (
        "user",
        "Job Description: {job_description}\n\nCandidate CV: {candidate_cv}\n\nStrictness of the Screening Process: {strictness_level}",
    ),
]
