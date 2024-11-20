project/
│
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
│
├── api_routes/                    # API routes
|   ├── __init__.py
│   ├── extraction_api.py   
│   ├── sql_database_api.py
|   ├── vector_database_api.py    
│
├── frontend/
│   ├── app.py              # Flask app serving APIs and front-end
│   ├── static/
│   ├── templates/
│
├── config/
|   ├── __init__.py
│   ├── config.py
├── storage/
│   ├── pdfs/          # For storing PDF files to be processed
│   ├── json_data/     # For saving extracted data in JSON format
│   ├── outputs/       # For generated outputs like final processed results, reports, etc.
│   └── logs/          # For logging information if needed
|   ├── sql/           # For storing sql database
├── utils.py
├── main.py
├── requirements.txt

