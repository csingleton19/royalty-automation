from flask import Blueprint, jsonify, request
from services.data_extraction.pdf_extractor import extract_and_save_pdf
from services.data_extraction.data_cleaner import data_cleaner
from services.information_extraction.extractor import extractor
from config.config import PDF_STORAGE_PATH
import os

# Create a Blueprint instance
extraction_api_blueprint = Blueprint("extraction_api", __name__)

@extraction_api_blueprint.route("/process-pdf", methods=["POST"])
def process_pdf():
    try:
        # Step 1: Get and save PDF
        pdf_file = request.files.get("pdf")
        if not pdf_file:
            return jsonify({"error": "No PDF file uploaded"}), 400
        
        filename = pdf_file.filename
        filepath = os.path.join(PDF_STORAGE_PATH, filename)
        pdf_file.save(filepath)
        
        # Step 2: Extract PDF to JSON
        extract_and_save_pdf(filepath)
        
        # Step 3: Clean the extracted text
        pickle_output = data_cleaner()
        if not pickle_output:
            return jsonify({"error": "Failed to clean the text data"}), 500
        
        # Step 4: Extract structured and unstructured data
        try:
            structured_data, unstructured_data = extractor()
        except Exception as e:
            return jsonify({"error": f"Data extraction failed: {str(e)}"}), 500
        
        return jsonify({
            "message": "PDF processed successfully",
            "structured_data": structured_data,
            "unstructured_data": unstructured_data
        })
        
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500



