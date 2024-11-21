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
│   ├── query_engine/
|       ├── __init__.py
|       ├── query_engine.py
|       ├── query_agent.py
│
├── api_routes/                    # API routes
|   ├── __init__.py
│   ├── extraction_api.py   
│   ├── sql_database_api.py
|   ├── vector_database_api.py    
│
frontend/
├── frontend-client/          # New React frontend
│   ├── src/
│   │   ├── components/      
│   │   ├── pages/          
│   │   ├── services/      
│   │   ├── types/         
│   │   └── utils/         
│   ├── package.json
│   └── tsconfig.json
└── app.py                  
│
├── config/
|   ├── __init__.py
│   ├── config.py
├── storage/
│   ├── csv/          
│   ├── json_data/    
│   ├── pdfs/       
│   └── pickles/          
|   ├── sql/           
├── utils.py
├── main.py
├── requirements.txt

