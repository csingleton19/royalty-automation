from flask import Blueprint, request, jsonify
from services.database.vector_database_handler import upload_embeddings

vector_db_api_blueprint = Blueprint('vector_db_api', __name__)

@vector_db_api_blueprint.route('/embeddings/upload', methods=['POST'])
def upload():
    raw_text = request.json.get('text')
    if not raw_text:
        return jsonify({"error": "No text provided"}), 400
    try:
        upload_embeddings(raw_text)
        return jsonify({"message": "Embeddings uploaded successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500