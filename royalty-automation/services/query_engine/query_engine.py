from services.database.sql_database_handler import sqlite3, DB_PATH
from services.database.vector_database_handler import index, get_embedding
from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
pinecone_api_key = os.getenv("PINECONE_KEY")

# Ensure the API key is loaded
if not pinecone_api_key:
    raise ValueError("PINECONE_KEY is not set in the environment variables.")

# Initialize Pinecone using the Pinecone class
pc = Pinecone(api_key=pinecone_api_key)
index_name = "royalties"

class QueryEngine:
    def __init__(self):
        self.vector_db = index  # Pinecone index from vector_database_handler
        self.sql_db_path = DB_PATH 

    def query_vector_db(self, query_text, top_k=2):
        """Query the vector database for similar entries"""
        try:
            # Generate embedding for query text
            query_embedding = get_embedding(query_text)
            
            # Search Pinecone index
            results = self.vector_db.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=True
            )
            return results
        except Exception as e:
            raise Exception(f"Vector database query failed: {str(e)}")

    def query_sql_db(self, query):
        """Query the SQL database"""
        try:
            with sqlite3.connect(self.sql_db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"SQL database query failed: {str(e)}")

    def route_query(self, query_type, query_params):
        """Route queries based on type"""
        if query_type == "semantic":
            return self.query_vector_db(query_params["text"])
        elif query_type == "structured":
            return self.query_sql_db(query_params["sql_query"])
        else:
            raise ValueError("Invalid query type")

# Usage example
if __name__ == "__main__":
    engine = QueryEngine()
    
    # Example semantic search
    semantic_query = {
        "type": "semantic",
        "params": {"text": "author biography"}
    }
    
    # Example structured query
    sql_query = {
        "type": "structured",
        "params": {"sql_query": "SELECT * FROM combined_data LIMIT 5"}
    }