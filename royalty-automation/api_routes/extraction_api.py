from flask import Blueprint, jsonify, request
from services.data_extraction.pdf_extractor import extract_and_save_pdf
from services.data_extraction.data_cleaner import data_cleaner
from services.information_extraction.extractor import extractor
from config.config import PDF_STORAGE_PATH
import os

# Create a Blueprint instance
extraction_api_blueprint = Blueprint("extraction_api", __name__)

@extraction_api_blueprint.route("/extract-pdf", methods=["POST"])
def extract_pdf():
    pdf_file = request.files.get("pdf")
    if not pdf_file:
        return jsonify({"error": "No PDF file uploaded"}), 400
    
    # Save uploaded file to storage
    filename = pdf_file.filename
    filepath = os.path.join(PDF_STORAGE_PATH, filename)
    pdf_file.save(filepath)
    
    # Process the saved file
    json_output = extract_and_save_pdf(filepath)
    
    return jsonify({"message": "PDF processed successfully", "output": json_output})

@extraction_api_blueprint.route("/clean-text", methods=["POST"])
def clean_text():
    """
    API endpoint to clean text from an uploaded JSON file.
    """
    # Process the JSON file directly using data_cleaner
    pickle_output = data_cleaner()  # No need to pass json_file if handled internally

    if not pickle_output:
        return jsonify({"error": "Failed to process the JSON file"}), 500

    # Return the Pickle file or metadata about it
    return jsonify({"message": "Text cleaned successfully", "output_file": pickle_output})

@extraction_api_blueprint.route("/extract-data", methods=["POST"])
def extractor_function():
    try:
        # Call the extractor function directly
        structured_data, unstructured_data = extractor()
        
        return jsonify({
            "message": "Data extracted successfully",
            "structured_data": structured_data,
            "unstructured_data": unstructured_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500



