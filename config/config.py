import os

# Base directory of the project (root directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Storage directories
CSV_STORAGE_PATH = os.path.join(BASE_DIR, "storage", "csv")
PICKLE_STORAGE_PATH = os.path.join(BASE_DIR, "storage", "pickles")
JSON_STORAGE_PATH = os.path.join(BASE_DIR, "storage", "json_data")
PDF_STORAGE_PATH = os.path.join(BASE_DIR, "storage", "pdfs")
SQL_STORAGE_PATH = os.path.join(BASE_DIR, "storage", "sql")


# Ensure storage directories exist
os.makedirs(PICKLE_STORAGE_PATH, exist_ok=True)
os.makedirs(JSON_STORAGE_PATH, exist_ok=True)
os.makedirs(CSV_STORAGE_PATH, exist_ok=True)
os.makedirs(PDF_STORAGE_PATH, exist_ok=True)
os.makedirs(SQL_STORAGE_PATH, exist_ok=True)

__all__ = ["BASE_DIR", "CSV_STORAGE_PATH", "PICKLE_STORAGE_PATH", "JSON_STORAGE_PATH", "PDF_STORAGE_PATH", "SQL_STORAGE_PATH"]
