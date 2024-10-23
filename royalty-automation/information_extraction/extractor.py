import os
import pickle
import openai
from config.config import BASE_DIR
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY")


# Use the BASE_DIR from config to construct the path
pkl_file_path = os.path.join(BASE_DIR, 'data_extraction', 'cleaned_data.pkl')

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
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    structured_data = response['choices'][0]['message']['content']
    
    # Convert the response to a dictionary if needed
    return structured_data  # You may want to parse it into a dict if it's in JSON format

def extract_unstructured_data_with_llm(data):
    """
    Uses OpenAI's API to extract unstructured data from the loaded data.
    """
    prompt = f"You are a royalty automation extraction tool. Ignore the structured data. Extract the unstructured, free-form, important information from the following: {data}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    unstructured_data = response['choices'][0]['message']['content']
    
    return unstructured_data

# Example usage
cleaned_data = load_cleaned_data()

if cleaned_data:
    structured_data = extract_structured_data_with_llm(cleaned_data)
    unstructured_data = extract_unstructured_data_with_llm(cleaned_data)

    print("Structured Data (Dictionary):")
    print(structured_data)
    
    print("\nUnstructured Data:")
    print(unstructured_data)




# Example usage
# if __name__ == "__main__":
#     data = load_cleaned_data()
#     if data is not None:
#         print("Cleaned data loaded successfully!")
#     else:
#         print("Failed to load cleaned data.")
#     extract_structured_data_with_llm(data)
#     extract_unstructured_data_with_llm(data)

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

