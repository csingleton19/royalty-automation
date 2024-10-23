import os
import json
from langchain_community.document_loaders import PyPDFLoader

# Function to extract raw text from a PDF
def extract_pdf_content(pdf_path: str):
    # Ensure the file exists before proceeding
    if not os.path.exists(pdf_path):
        raise ValueError(f"File path {pdf_path} does not exist. Please check the path.")
    
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()  # Extracts document data
    raw_text = " ".join([doc.page_content for doc in documents])  # Combines all the pages' content
    return raw_text

# Function to save extracted data into a JSON file
def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file)

# Function to search for PDF files in the current working directory (CWD)
def find_pdf_in_cwd():
    cwd = os.getcwd()  # Get current working directory
    pdf_files = [file for file in os.listdir(cwd) if file.endswith('.pdf')]
    return pdf_files

# Function to handle PDF extraction workflow
def extract_and_save_pdf():
    pdf_files = find_pdf_in_cwd()

    if pdf_files:
        print(f"Found the following PDF files in CWD: {pdf_files}")
        pdf_path = pdf_files[0]  # Automatically selecting the first found PDF
        print(f"Extracting from: {pdf_path}")
    else:
        # If no PDFs found, prompt user for input
        pdf_path = input("No PDF found in the CWD. Please drag and drop a PDF file, or provide the full path: ").strip()
        
        # Sanitize the path (strip extra spaces and handle quotes)
        pdf_path = pdf_path.strip().strip('"').strip("'")

    # Validate that the file path exists before proceeding
    if not os.path.isfile(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist or is not a valid file.")
        return

    # Extract content from the selected or provided PDF path
    extracted_text = extract_pdf_content(pdf_path)

    # Save raw content to JSON
    output_file = "extracted_data.json"
    data = {"pdf_text": extracted_text}
    save_to_json(data, output_file)

    print(f"Extracted data has been saved to {output_file}")

# Example usage
if __name__ == "__main__":
    extract_and_save_pdf()

