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



# def clean_extracted_text(json_data):
#     # Step 1: Reorder titles and data, ensure title comes before data
#     lines = text.split('\n')
#     clean_lines = []
#     temp_storage = []
    
#     for line in lines:
#         # If a line contains 'QX YYYY Royalty Statement', store it temporarily for reordering
#         if re.match(r'Q[1-4] \d{4} Royalty Statement', line):
#             temp_storage.append(line)  # Store the title
#         else:
#             # Append stored title if we hit data after it
#             if temp_storage:
#                 clean_lines.append(temp_storage.pop(0))  # Append the stored title
#             clean_lines.append(line)
    
#     # Add any remaining titles at the end (if any were not matched with data)
#     clean_lines.extend(temp_storage)
    
#     # Step 2: Fix split words, using regex to find and replace splits (like T aylor to Taylor)
#     joined_text = ' '.join(clean_lines)
#     fixed_text = re.sub(r'\b(\w)\s+(\w+)', r'\1\2', joined_text)  # Fix simple word splits
    
#     # Step 3: Remove unnecessary spaces or newlines between connected text
#     fixed_text = re.sub(r'\n+', '\n', fixed_text)  # Normalize multiple newlines
#     fixed_text = re.sub(r'\s{2,}', ' ', fixed_text)  # Normalize multiple spaces
    
#     # Step 4: Ensure tables stay readable by fixing tabular data spacing
#     # Example: If there are more than one space separating items in a line, replace with a single space
#     table_cleaned = re.sub(r' {2,}', ' ', fixed_text)
#     print(table_cleaned)
#     return table_cleaned

# # Example of how you'd call this function
# extracted_text = """
# Q1 2024 Royalty Statement
# Author Advance Earned Total Sales Royalty (%) Gross Earnings Deductions Net Earnings
# Alice Johnson 1000 5000 10 500 50 450
# Bob Smith 1500 3000 12 360 30 330
# Carol T aylor 2000 4000 15 600 40 560
# T otal 4500 12000 - 1460 120 1340
# """

# cleaned_text = clean_extracted_text(extracted_text)
# print(cleaned_text)
