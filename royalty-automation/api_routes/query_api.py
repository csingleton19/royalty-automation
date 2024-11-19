from flask import Blueprint, request, jsonify
from services.query_engine.query_engine import QueryEngine

query_api_blueprint = Blueprint('query_api', __name__)
engine = QueryEngine()

@query_api_blueprint.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        query_type = data.get('type')
        query_params = data.get('params')
        
        results = engine.route_query(query_type, query_params)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500