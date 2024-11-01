import os
import pickle
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
    Uses OpenAI's API to extract structured data and format it as a dictionary.
    """
    prompt = f"""You are a royalty automation extraction tool. Ignore the unstructured data 
    Extract and format the structured data as a dictionary from the following: 
    {data}
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    structured_data = response.choices[0].message
    
    return structured_data  

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
    
    unstructured_data = response.choices[0].message
    
    return unstructured_data


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
    else:
        print("Failed to load cleaned data.")

