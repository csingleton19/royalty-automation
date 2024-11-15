from flask import Flask, render_template, request, jsonify
from api.extraction_api import extraction_api_blueprint  # Import API blueprints
from api.sql_database_api import sql_db_api_blueprint
from api.vector_database_api import vector_db_api_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(extraction_api_blueprint, url_prefix="/api/extraction")
app.register_blueprint(sql_db_api_blueprint, url_prefix="/api/sql")
app.register_blueprint(vector_db_api_blueprint, url_prefix="/api/vector")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
