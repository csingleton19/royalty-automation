from services.query_engine.query_engine import QueryEngine
# import openai
import os
from openai import OpenAI
from config.config import BASE_DIR
from dotenv import load_dotenv
from typing import Dict, Any, List, Union
import json

# Load environment variables from .env file
load_dotenv()
# Set the OpenAI API key
client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

class QueryAgent:
    def __init__(self):
        self.query_engine = QueryEngine()
        
    def analyze_query_intent(self, query: str) -> Dict[str, Any]:
        """Determine the best query strategy using OpenAI"""
        system_prompt = """
        Analyze the query and determine:
        1. If it needs semantic search (return "semantic")
        2. If it needs structured SQL (return "structured")
        3. If it needs both (return "hybrid")
        Return as JSON with fields: query_type, params
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            response_format={ "type": "json_object" }
        )
        
        return json.loads(response.choices[0].message.content)

    def format_sql_query(self, intent: Dict[str, Any]) -> str:
        """Convert intent parameters into SQL query"""
        #testing
        if "author" in intent:
            return f"SELECT * FROM combined_data WHERE author = '{intent['author']}'"
        elif "date" in intent:
            return f"SELECT * FROM combined_data WHERE date = '{intent['date']}'"
        return "SELECT * FROM combined_data LIMIT 5"  # fallback

    def combine_results(self, semantic_results: List, sql_results: List) -> Dict[str, Any]:
        """Combine and format results from multiple sources"""
        return {
            "semantic_results": semantic_results,
            "sql_results": sql_results,
            "combined": {
                "total_results": len(semantic_results) + len(sql_results),
                "sources": ["vector_db", "sql_db"]
            }
        }

    def process_query(self, user_query: str) -> Dict[str, Any]:
        """Main entry point for processing queries"""
        try:
            # Analyze query intent
            intent = self.analyze_query_intent(user_query)
            results = []

            # Route based on intent
            if intent["query_type"] == "semantic":
                results = self.query_engine.query_vector_db(
                    query_text=user_query,
                    top_k=2
                )
                return {"results": results, "type": "semantic"}

            elif intent["query_type"] == "structured":
                sql_query = self.format_sql_query(intent["params"])
                results = self.query_engine.query_sql_db(sql_query)
                return {"results": results, "type": "structured"}

            elif intent["query_type"] == "hybrid":
                semantic_results = self.query_engine.query_vector_db(
                    query_text=user_query,
                    top_k=3
                )
                sql_query = self.format_sql_query(intent["params"])
                sql_results = self.query_engine.query_sql_db(sql_query)
                
                return self.combine_results(semantic_results, sql_results)

            else:
                raise ValueError(f"Unsupported query type: {intent['query_type']}")

        except Exception as e:
            return {"error": str(e), "query": user_query}