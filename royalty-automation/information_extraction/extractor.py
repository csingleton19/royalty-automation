import os
import pickle
from config.config import BASE_DIR


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

# Example usage
if __name__ == "__main__":
    data = load_cleaned_data()
    if data is not None:
        print("Cleaned data loaded successfully!")
    else:
        print("Failed to load cleaned data.")

