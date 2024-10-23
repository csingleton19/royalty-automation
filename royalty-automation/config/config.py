import os

# Base directory of the project (root directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# add other configurations here later i.e. I'm going to use Pinecone for vector database and SQLite3 for tabular data
# e.g. DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'db.sqlite3')
