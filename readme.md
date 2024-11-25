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
├── requirements.txt
'''


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