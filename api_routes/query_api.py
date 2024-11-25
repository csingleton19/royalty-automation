from flask import Blueprint, request, jsonify
from services.query_engine.query_agent import QueryAgent

query_api_blueprint = Blueprint('query_api', __name__)
agent = QueryAgent()

@query_api_blueprint.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        user_query = data.get('query')
        
        if not user_query:
            return jsonify({"error": "No query provided"}), 400
            
        results = agent.process_query(user_query)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500