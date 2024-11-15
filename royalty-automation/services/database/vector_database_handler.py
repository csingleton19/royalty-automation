import os
import json
import openai
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()
pinecone_api_key = os.getenv("PINECONE_KEY")
openai_api_key = os.getenv("OPENAI_KEY")

# Set OpenAI API key directly
openai.api_key = openai_api_key
client = openai.OpenAI(api_key=os.environ.get("OPENAI_KEY"))

# Initialize Pinecone using the Pinecone class
pc = Pinecone(api_key=pinecone_api_key)
index_name = "royalties"

# Check if the Pinecone index exists by name
existing_indexes = [index['name'] for index in pc.list_indexes()]
print(existing_indexes)
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='cosine',  # Set the metric to cosine, dot_product, or euclidean
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(index_name)


# Function to get embeddings from OpenAI
def get_embedding(text, model="text-embedding-ada-002"):
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding  # Extract embedding vector

# Function to parse biographies from raw text
def parse_biographies(raw_text):
    bios = raw_text.split('\n\n')
    data = []
    for i, bio in enumerate(bios):
        data.append({"id": str(i+1), "text": bio.strip()})
    return data

# Function to upload embeddings to Pinecone
def upload_embeddings(raw_text):
    data = parse_biographies(raw_text)
    embeddings = []
    for item in data:
        text = item['text']
        vector = get_embedding(text)  # Get embedding from OpenAI
        embeddings.append({"id": item['id'], "values": vector})  # Use unique IDs if possible

    # Upload to Pinecone
    index.upsert(vectors=embeddings)

if __name__ == "__main__":
    with open("storage/json_data/output_data.json", 'r') as f:
        raw_text = f.read()
    upload_embeddings(raw_text)


