project/
│
├── services/               # Core functionality
│   ├── data_extraction/
│       ├── pdf_extractor.py
│       ├── data_cleaner.py
│   ├── information_extraction/
|       ├── extractor.py
│   ├── database/
|       ├── sql_dabatase_handler.py
|       ├── vector_database_handler.py
│
├── api/                    # API routes
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
│   ├── config.py
├── storage/
│   ├── pdfs/          # For storing PDF files to be processed
│   ├── json_data/     # For saving extracted data in JSON format
│   ├── outputs/       # For generated outputs like final processed results, reports, etc.
│   └── logs/          # For logging information if needed
├── utils.py
├── main.py
├── requirements.txt

