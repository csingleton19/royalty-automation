import os
import pickle
import json
import pandas as pd
from openai import OpenAI
from config.config import BASE_DIR
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Set the OpenAI API key
# OpenAI.api_key = os.getenv("OPENAI_KEY")
# client = (OpenAI.api_key)
client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

# Use the BASE_DIR from config to construct the path
pkl_file_path = os.path.join(BASE_DIR, 'storage/pickles', 'cleaned_data.pkl')

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
    Ensure the output is in a valid JSON format, only include the nested dictionary. 
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

def create_quarterly_dataframes(structured_data):
    quarterly_dfs = {}
    for quarter, details in structured_data.items():
        # Create DataFrame for the total summary
        total_df = pd.DataFrame([details["Total"]])
        
        # Create DataFrame for the individual authors
        authors_df = pd.DataFrame(details["Authors"])
        
        # Store both in a dictionary for easy access
        quarterly_dfs[quarter] = {"total": total_df, "authors": authors_df}
    return quarterly_dfs

if __name__ == "__main__":
    data = load_cleaned_data()
    if data is not None:
        print("Cleaned data loaded successfully!")
        
        structured_data = extract_structured_data_with_llm(data)
        unstructured_data = extract_unstructured_data_with_llm(data)
        
        print("Structured Data (Dictionary):")
        print(structured_data)
        
        print("\nUnstructured Data:")
        print(unstructured_data)

         # Ensure structured_data is a dictionary before proceeding
        if isinstance(structured_data, dict) and structured_data:
            quarterly_dfs = create_quarterly_dataframes(structured_data)
            for quarter, dfs in quarterly_dfs.items():
                print(f"\n{quarter} - Total Summary:")
                print(dfs["total"])
                print(f"\n{quarter} - Authors:")
                print(dfs["authors"])
        else:
            print("Structured data is not in dictionary format. Please check the extraction.")
    else:
        print("Failed to load cleaned data.")