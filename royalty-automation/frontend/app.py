from flask import Flask, render_template, request, jsonify
from config.config import BASE_DIR
from api_routes.extraction_api import extraction_api_blueprint  # Import API blueprints
from api_routes.sql_database_api import sql_db_api_blueprint
from api_routes.vector_database_api import vector_db_api_blueprint
from api_routes.query_api import query_api_blueprint
# from config.config import JSON_STORAGE_PATH


app = Flask(__name__)


# Register Blueprints
app.register_blueprint(extraction_api_blueprint, url_prefix="/api/extraction")
app.register_blueprint(sql_db_api_blueprint, url_prefix="/api/sql")
app.register_blueprint(vector_db_api_blueprint, url_prefix="/api/vector")
app.register_blueprint(query_api_blueprint,"api/query" )

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
