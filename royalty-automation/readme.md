|royalty-automation/
│
|
├── api_routes/                    # API routes
|   ├── __init__.py
│   ├── extraction_api.py  
|   ├── query_api.py 
│   ├── sql_database_api.py
|   ├── vector_database_api.py   
| 
├── config/
|   ├── __init__.py
│   ├── config.py
|
frontend/
├── client/
│   ├── src/
│   │   ├── components/
│   │   │   ├── DatabaseManager.tsx
│   │   │   ├── Navigation.tsx
│   │   │   ├── PDFUploader.tsx
│   │   │   ├── QueryInterface.tsx
│   │   │   └── VectorDBManager.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   │   └── index.ts
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── App.test.tsx
│   │   ├── index.tsx
│   │   ├── index.css
│   │   ├── react-app-env.d.ts
│   │   ├── reportWebVitals.ts
│   │   └── setupTests.ts
│   ├── public/
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── .gitignore
│   ├── README.md
│   ├── package.json
│   └── tsconfig.json
├── __init__.py
└── app.py
|
├── node_modules
|
├── services/               # Core functionality
│   ├── data_extraction/
|       ├── __init__.py
│       ├── pdf_extractor.py
│       ├── data_cleaner.py
│   ├── information_extraction/
|       ├── __init__.py
|       ├── extractor.py
│   ├── database/
|       ├── __init__.py
|       ├── sql_dabatase_handler.py
|       ├── vector_database_handler.py
│   ├── query_engine/
|       ├── __init__.py
|       ├── query_engine.py
|       ├── query_agent.py                 
│
├── storage/
│   ├── csv/          
│   ├── json_data/    
│   ├── pdfs/       
│   └── pickles/          
|   ├── sql/           
├── utils.py
├── main.py
├── requirements.txt



TODO:
Fix response structures 
*vector_db: special characters/newline characters, return only text (not entire output)
*SQL: results aren't specific enough