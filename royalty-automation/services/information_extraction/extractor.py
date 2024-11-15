import os
import pickle
import json
import pandas as pd
from openai import OpenAI
from config.config import BASE_DIR
from dotenv import load_dotenv
from config import PICKLE_STORAGE_PATH

# Load environment variables from .env file
load_dotenv()
# Set the OpenAI API key
client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

# Use the BASE_DIR from config to construct the path
pkl_file_path = os.path.join(PICKLE_STORAGE_PATH, 'cleaned_data.pkl')

def load_cleaned_data():
    try:
        with open(pkl_file_path, 'rb') as file:
            cleaned_data = pickle.load(file)
        return cleaned_data
    except FileNotFoundError:
        print(f"Error: The file {pkl_file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the pickle file: {e}")
        return None


def extract_structured_data_with_llm(data):
    """
    Uses OpenAI's API to extract structured data, format it as a dictionary,
    and then parse it into a nested Python dictionary.
    """
    prompt = f"""You are a royalty automation extraction tool. Ignore any unstructured data 
    and extract and format only the structured data as a nested dictionary from the following: 
    {data}
    Ensure the output is in a valid JSON format, only include the nested dictionary. Name the nested dictionary 'royalties'
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format={ "type": "json_object" }
    )
    
    # Extract the response content (string format) from the LLM
    structured_data_str = response.choices[0].message.content

    # return structured_data_str
    
    try:
        # Parse the string into a nested dictionary using json.loads
        structured_data_dict = json.loads(structured_data_str)
    except json.JSONDecodeError:
        raise ValueError("The LLM response is not in a valid JSON format.")
    
    return structured_data_dict


def extract_unstructured_data_with_llm(data):
    """
    Uses OpenAI's API to extract unstructured data from the loaded data.
    """
    prompt = f"You are a royalty automation extraction tool. Ignore the structured data. Extract the unstructured, free-form, important information from the following: {data}"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    unstructured_data = response.choices[0].message.content
    
    return unstructured_data

def extract_and_save_authors_data(structured_data):
    # Ensure "RoyaltyStatements" exists in the structured data
    if "royalties" not in structured_data:
        print("No 'royalties' data found.")
        return
    
    # Access the quarterly data within "royalties"
    quarterly_data = structured_data["royalties"]
    all_authors_dfs = []
    
    # Iterate over each quarter
    for quarter, details in quarterly_data.items():
        # Check if "Authors" is in the details for the quarter
        if "Authors" not in details:
            print(f"No 'Authors' data found for {quarter}")
            continue
        
        # Process authors' data for the current quarter
        authors_data = []
        for author_info in details["Authors"]:
            # Assume author_info is a dictionary with all author metrics
            author_data = {"Quarter": quarter}
            author_data.update(author_info)  # Include all author info
            authors_data.append(author_data)
        
        # Create a DataFrame for the current quarter's authors
        authors_df = pd.DataFrame(authors_data)
        all_authors_dfs.append(authors_df)
    
    # Concatenate all author data across quarters
    if all_authors_dfs:
        combined_df = pd.concat(all_authors_dfs, ignore_index=True)
        
        # Define the directory and filename for the CSV using BASE_DIR directly
        csv_dir = os.path.join(BASE_DIR, 'storage/csv')
        os.makedirs(csv_dir, exist_ok=True)
        csv_file_path = os.path.join(csv_dir, 'combined_data.csv')
        
        # Save the DataFrame to a CSV file
        combined_df.to_csv(csv_file_path, index=False)
        print(f"Combined authors' data saved to {csv_file_path}")
    else:
        print("No author data found across all quarters.")



def save_data_as_json(data, file_name, base_dir='storage/json_data'):
    """
    Saves unstructured or semi-structured data to a JSON file.
    
    Args:
        data (dict or list): The data to save, ideally in dictionary or list format.
        file_name (str): The desired name of the JSON file, without extension.
        base_dir (str): The directory path to save the JSON file.
    """
    # Construct the path and ensure directory exists
    json_file_path = os.path.join(base_dir, f'{file_name}.json')
    os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
    
    # Save the data as JSON
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {json_file_path}")


if __name__ == "__main__":
    data = load_cleaned_data()
    if data is not None:
        print("Cleaned data loaded successfully!")
        
        structured_data = extract_structured_data_with_llm(data)
        unstructured_data = extract_unstructured_data_with_llm(data)
        print("Structured Data (Dictionary):")
        print(structured_data)
        print("Unstructured Data:")
        print(unstructured_data)

        # Save the combined authors' data to CSV
        if isinstance(structured_data, dict) and structured_data:
            extract_and_save_authors_data(structured_data)
        else:
            print("Structured data is not in dictionary format. Please check the extraction.")
        
        save_data_as_json(unstructured_data, 'output_data')
    else:
        print("Failed to load cleaned data.")