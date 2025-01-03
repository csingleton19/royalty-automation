import os
import json
from langchain_community.document_loaders import PyPDFLoader
from config import PDF_STORAGE_PATH, JSON_STORAGE_PATH

# Function to extract raw text from a PDF
def extract_pdf_content(pdf_path: str):
    if not os.path.exists(pdf_path):
        raise ValueError(f"File path {pdf_path} does not exist. Please check the path.")
    
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()  # Extracts document data
    raw_text = " ".join([doc.page_content for doc in documents])  # Combines all pages' content
    return raw_text

# Function to save extracted data into a JSON file
def save_to_json(data, output_file_name):
    output_path = os.path.join(JSON_STORAGE_PATH, output_file_name)
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file)
    print(f"Data saved to {output_path}")

# Function to search for PDF files in the centralized PDF storage directory
def find_pdf_in_storage():
    pdf_files = [file for file in os.listdir(PDF_STORAGE_PATH) if file.endswith('.pdf')]
    return pdf_files

def extract_and_save_pdf(pdf_path: str = None):
    """
    Handles PDF extraction workflow.
    - If `pdf_path` is provided, it extracts content from that file.
    - If `pdf_path` is None, it searches for the first available PDF in storage.
    """
    if not pdf_path:
        pdf_files = find_pdf_in_storage()
        if not pdf_files:
            raise ValueError("No PDF files found in storage. Please upload a PDF.")
        pdf_path = os.path.join(PDF_STORAGE_PATH, pdf_files[0])  # Use the first available PDF
        print(f"Extracting from: {pdf_path}")

    if not os.path.isfile(pdf_path):
        raise ValueError(f"File '{pdf_path}' does not exist or is not a valid file.")

    # Extract content from the selected or provided PDF path
    extracted_text = extract_pdf_content(pdf_path)

    # Save raw content to JSON
    output_file_name = "extracted_data.json"
    data = {"pdf_text": extracted_text}
    save_to_json(data, output_file_name)

    print(f"Extracted data has been saved to {os.path.join(JSON_STORAGE_PATH, output_file_name)}")


# Example usage
if __name__ == "__main__":
    extract_and_save_pdf()



