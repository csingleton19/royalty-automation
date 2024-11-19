from flask import Blueprint, request, jsonify
from services.database.vector_database_handler import upload_embeddings

vector_db_api_blueprint = Blueprint('vector_db_api', __name__)

@vector_db_api_blueprint.route('/embeddings/upload', methods=['POST'])
def upload():
    try:
        # Read from output_data.json
        with open("storage/json_data/output_data.json", 'r') as f:
            raw_text = f.read()
        
        if not raw_text:
            return jsonify({"error": "No text found in output_data.json"}), 400
            
        upload_embeddings(raw_text)
        return jsonify({"message": "Embeddings uploaded successfully."})
    except FileNotFoundError:
        return jsonify({"error": "output_data.json not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
