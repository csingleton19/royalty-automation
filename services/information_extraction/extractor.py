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
            
        # Validate the data
        if not cleaned_data or not isinstance(cleaned_data, str):
            raise ValueError("Invalid cleaned data format")
            
        return cleaned_data
    except FileNotFoundError:
        print(f"Error: The file {pkl_file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the pickle file: {e}")
        return None

def extract_structured_data_with_llm(data):
    prompt = f"""You are a royalty automation extraction tool. Ignore any unstructured data 
    and extract and format only the structured data as a nested dictionary from the following: 
    {data}
    Ensure the output is in a valid JSON format, only include the nested dictionary. Name the nested dictionary 'royalties'
    and ensure each quarter contains an 'Authors' key (uppercase) with an array of author data.
    Each author entry must use 'Name' (not 'Author') as the key for the author's name.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format={ "type": "json_object" }
    )
    
    structured_data_str = response.choices[0].message.content
    
    try:
        structured_data_dict = json.loads(structured_data_str)
        return structured_data_dict
    except json.JSONDecodeError:
        raise ValueError("The LLM response is not in a valid JSON format.")

def extract_unstructured_data_with_llm(data):
    """
    Uses OpenAI's API to extract unstructured data from the loaded data.
    """
    prompt = f"""You are a royalty automation extraction tool. Extract and format the unstructured data following these rules:
    1. Use markdown formatting
    2. Format author names as headers with '**'
    3. Use bullet points for all biographical information
    4. Italicize book titles with '*'
    5. Separate sections with blank lines
    6. Format financial insights as bullet points
    7. Keep sentences concise
    
    Extract from the following: {data}"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    unstructured_data = response.choices[0].message.content
    return unstructured_data

def extract_and_save_authors_data(structured_data):
    if "royalties" not in structured_data:
        print("No 'royalties' data found.")
        return
    
    quarterly_data = structured_data["royalties"]
    all_authors_dfs = []
    
    for quarter, details in quarterly_data.items():
        if "Authors" not in details:
            print(f"No 'Authors' data found for {quarter}")
            continue
        
        authors_data = []
        for author_info in details["Authors"]:
            # Normalize the author data
            author_data = {"Quarter": quarter}
            # Handle both "Name" and "Author" keys
            if "Name" in author_info:
                author_data["Name"] = author_info["Name"]
            elif "Author" in author_info:
                author_data["Name"] = author_info["Author"]
            else:
                print(f"No author name found in entry: {author_info}")
                continue
                
            for key, value in author_info.items():
                if key not in ["Name", "Author"]:  
                    author_data[key] = value
                    
            authors_data.append(author_data)
        
        if authors_data:
            authors_df = pd.DataFrame(authors_data)
            all_authors_dfs.append(authors_df)
    
    if all_authors_dfs:
        combined_df = pd.concat(all_authors_dfs, ignore_index=True)
        csv_dir = os.path.join(BASE_DIR, 'storage/csv')
        os.makedirs(csv_dir, exist_ok=True)
        csv_file_path = os.path.join(csv_dir, 'combined_data.csv')
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

def extractor():
    """
    Function that combines all of the logic
    """
    try:
        data = load_cleaned_data()
        if data is None:
            raise ValueError("Failed to load cleaned data")
            
        try:
            structured_data = extract_structured_data_with_llm(data)
        except Exception as e:
            print(f"Error in structured data extraction: {e}")
            raise
            
        try:
            unstructured_data = extract_unstructured_data_with_llm(data)
        except Exception as e:
            print(f"Error in unstructured data extraction: {e}")
            raise
        
        # Save the combined authors' data to CSV
        if isinstance(structured_data, dict) and structured_data:
            try:
                extract_and_save_authors_data(structured_data)
            except Exception as e:
                print(f"Error saving authors data: {e}")
                raise
        
        save_data_as_json(unstructured_data, 'output_data')
        
        return structured_data, unstructured_data
    except Exception as e:
        print(f"Error in extractor: {e}")
        raise


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