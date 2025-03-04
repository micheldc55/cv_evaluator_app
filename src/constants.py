BASE_DIR = "candidates"

# used to keep our status names consistent
APPROVED = "approved"
REJECTED = "rejected"
PENDING = "pending"
SKIPPED = "skipped"

STATUS_COLOR_MAPPING = {
    "APPROVED": "#2E8B57",
    "REJECTED": "#D32F2F",
    "PENDING": "#FBC02D", 
    "SKIPPED": "#757575", 
}

PDF_WIDTH = 1500
PDF_HEIGHT = 1500

APP_PAGES = ["Upload CVs", "Evaluate Candidate", "Interview", "Overview"]

#### DOCUMENT CONFIGS
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

STRICTNESS_LEVELS = ["Very Strict", "Moderately Strict", "Moderately Lenient", "Very Lenient"]