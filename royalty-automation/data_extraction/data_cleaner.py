import re
import json
import os

def load_json_file(filename):
    """Load a JSON file from the current directory or prompt for a new file."""
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    else:
        # Ask the user to provide a filepath
        print(f"{filename} not found. Please provide the path to the JSON file.")
        filepath = input("You can drag and drop the file here or enter the file path: ")

        # Check if the provided path exists
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)
                return data
        else:
            print("The provided file path is invalid. Please check and try again.")
            return None

# Replace 'extracted_data.json' with your desired JSON filename
filename = 'extracted_data.json'
json_data = load_json_file(filename)

if json_data is not None:
    print("JSON data loaded successfully.")
    # Extract the actual text from the JSON data
    extracted_text = json_data.get('pdf_text', '')
else:
    print("Failed to load JSON data.")
    extracted_text = ''

def clean_extracted_text(text):
    # Fix split words like "T aylor" -> "Taylor"
    text = re.sub(r'\b([A-Za-z])\s([A-Za-z])', r'\1\2', text)
    
    # Handle cases where the title is placed after the data
    text = re.sub(r'(?<=\d{4}\s(?:Royalty Statement))\s+(.*?)(Author\s.*?)(\sQ\d)', r'\2\n\1\3', text, flags=re.DOTALL)
    
    # Remove unnecessary spaces and newlines between data
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'\s{2,}', ' ', text)

    # Remove unnecessary line breaks in paragraphs (for biographies)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    # Align table-like structures by ensuring the columns have consistent spacing
    text = re.sub(r'(?<=\d)\s+(?=\d)', ' ', text)  # Handle spaces in numeric data

    # Remove any trailing spaces at the end of lines
    text = re.sub(r'[ \t]+$', '', text, flags=re.M)
    
    return text

# Clean the extracted text
if extracted_text:
    cleaned_text = clean_extracted_text(extracted_text)
    print("Cleaned Text:")
    print(cleaned_text)
else:
    print("No text to clean.")

