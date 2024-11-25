# Index:

1. Introduction
2. Setup
3. Discussion
4. Limitations
5. Future Work
6. Structure

# Introduction:

This project started over a year ago when someone reached out to me about an idea they had for royalty automation as apparently royalties for authors are calculated manually, therefore automating it could free up a lot of time for those agents. I built a rough MVP using Python, LangChain, OpenAI, and Pinecone - however the other person had to step away. Between that, major framework updates, and someone pointing out a few improvements I could make, I decided to just rewrite the entire thing while keeping in mind the things I like from the previous iteration. A lot of the changes came from OpenAI i.e. I used to use openai.ChatCompletions.create - but that was deprecated in the v.0 versions, and I wanted to use the latest versions. 

# Setup:

# Discussion:

# Limitations

# Future Work

TODO:
1. Fix response structures 

*vector_db: remove special characters/newline characters, return only text (not entire pinecone output)

*SQL: results aren't specific enough i.e. Alice Johnson Q1 query returns all author Q1 and 2 Q2 results 

2. Hardcoding certain filepaths
3. Certain naming conventions could be better
4. Maybe a little more modularity (i.e. extractor)
5. Embedding process in that it should allow for larger document sizes (chunking + cross chunk context preservation via a sentence or two overlapping)
6. Definitely need to work on how SQL tables are created and handled - this and #1 are most important I think (also ties into 3 a little bit, slightly redundant)
7. Fix the headers so they also get uploaded to SQL


# Structure


```plaintext
royalty-automation/
├── api_routes/
│   ├── __init__.py
│   ├── extraction_api.py
│   ├── query_api.py
│   ├── sql_database_api.py
│   ├── vector_database_api.py
├── config/
│   ├── __init__.py
│   ├── config.py
├── frontend/
│   ├── client/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── DatabaseManager.tsx
│   │   │   │   ├── Navigation.tsx
│   │   │   │   ├── PDFUploader.tsx
│   │   │   │   ├── QueryInterface.tsx
│   │   │   │   └── VectorDBManager.tsx
│   │   │   ├── services/
│   │   │   │   └── api.ts
│   │   │   ├── types/
│   │   │   │   └── index.ts
│   │   │   ├── App.tsx
│   │   │   ├── App.css
│   │   │   ├── App.test.tsx
│   │   │   ├── index.tsx
│   │   │   ├── index.css
│   │   │   ├── react-app-env.d.ts
│   │   │   ├── reportWebVitals.ts
│   │   │   └── setupTests.ts
│   │   ├── public/
│   │   │   ├── index.html
│   │   │   ├── manifest.json
│   │   │   └── robots.txt
│   │   ├── .gitignore
│   │   ├── README.md
│   │   ├── package.json
│   │   └── tsconfig.json
├── node_modules/
├── services/  # Core functionality
│   ├── data_extraction/
│   │   ├── __init__.py
│   │   ├── pdf_extractor.py
│   │   └── data_cleaner.py
│   ├── information_extraction/
│   │   ├── __init__.py
│   │   └── extractor.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── sql_database_handler.py
│   │   └── vector_database_handler.py
│   ├── query_engine/
│   │   ├── __init__.py
│   │   ├── query_engine.py
│   │   └── query_agent.py
│   ├── storage/
│   │   ├── csv/
│   │   ├── json_data/
│   │   ├── pdfs/
│   │   └── pickles/
│   └── sql/
├── utils.py
├── main.py
├── requirements.txt'''


# Setup 

