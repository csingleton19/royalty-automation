from flask import Blueprint, jsonify
from services.database.sql_database_handler import initialize_database, load_data_into_database

sql_db_api_blueprint = Blueprint('sql_db_api', __name__)

@sql_db_api_blueprint.route('/database/initialize', methods=['POST'])
def initialize():
    try:
        initialize_database()
        return jsonify({"message": "Database initialized successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@sql_db_api_blueprint.route('/database/load', methods=['POST'])
def load_data():
    try:
        load_data_into_database()
        return jsonify({"message": "Data loaded into database successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

