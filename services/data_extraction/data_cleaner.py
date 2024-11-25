import os
import re
import json
import pickle
from config import PICKLE_STORAGE_PATH, JSON_STORAGE_PATH

def load_json_file(filename):
    """Load a JSON file from the centralized JSON storage or prompt for a new file."""
    filepath = os.path.join(JSON_STORAGE_PATH, filename)
    
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    else:
        print(f"{filename} not found in {JSON_STORAGE_PATH}. Please provide the path to the JSON file.")
        return None

def clean_extracted_text(text):
    """Clean the extracted text by applying various formatting rules."""
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
    
    # Clean up biography headers and formatting
    text = re.sub(r'(\w+)\s*:\s*\n', r'**\1:**\n', text)
    
    # Convert paragraph style biographies to bullet points
    text = re.sub(r'(?<=\n)(?![-•*])\s*([^:\n][^\n]+?)(?=\n)', r'- \1', text)
    
    # Clean up multiple spaces between bullet points
    text = re.sub(r'\n\s*-\s+', '\n- ', text)
    
    # Format book titles consistently
    text = re.sub(r'(["\'])(.*?)\1', r'*\2*', text)
    
    # Add proper spacing between sections
    text = re.sub(r'(\*\*[^*]+:\*\*)\n', r'\1\n\n', text)
    
    # Clean up financial insights formatting
    text = re.sub(r'(Financial Insights[^\n]*:)\n', r'**\1**\n\n', text)
    
    return text
    
def save_cleaned_text_as_pickle(cleaned_text, filename='cleaned_data.pkl'):
    """Save the cleaned text as a pickle file."""
    pickle_path = os.path.join(PICKLE_STORAGE_PATH, filename)
    
    # Save the cleaned text using pickle
    with open(pickle_path, 'wb') as pickle_file:
        pickle.dump(cleaned_text, pickle_file)
    print(f"Cleaned text saved as {pickle_path}")

def data_cleaner():
    """Main function to orchestrate the process."""
    filename = 'extracted_data.json'
    json_data = load_json_file(filename)

    if json_data is not None:
        print("JSON data loaded successfully.")
        extracted_text = json_data.get('pdf_text', '')
    else:
        print("Failed to load JSON data.")
        return None

    if extracted_text:
        cleaned_text = clean_extracted_text(extracted_text)
        print("Cleaned Text:")
        print(cleaned_text)
        
        # Save and return the output filename
        output_filename = 'cleaned_data.pkl'
        save_cleaned_text_as_pickle(cleaned_text, filename=output_filename)
        return output_filename
    else:
        print("No text to clean.")
        return None

if __name__ == "__main__":
    data_cleaner()






