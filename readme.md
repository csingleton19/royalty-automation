# Index:

1. Introduction
2. Setup
3. Discussion
4. Limitations
5. Future Work
6. Structure

# Introduction:

This project started over a year ago when someone reached out to me about an idea they had for royalty automation as apparently royalties for authors are calculated manually, therefore automating it could free up a lot of time for those agents. I built a rough MVP using Python, LangChain, OpenAI, and Pinecone - however the other person had to step away. Between that, major framework updates, and someone pointing out a few improvements I could make, I decided to just rewrite the entire thing while keeping in mind the things I like from the previous iteration. A lot of the changes came from OpenAI i.e. I used to use openai.ChatCompletions.create - but that was deprecated in the v.0 versions, and the v1 versions don't play well with the v0 versions. Keep in mind this project (as of v.0.1.0) is functional, but ugly in some ways (see Limitations section) - however, I am happy with it considering the stage it is in!

# Setup:

The setup for this is really left as an exercise to the reader for v.0.1.0 - when I implement a few of the upgrades mentioned in the later Future Work sections, I'll finalize a v1.0.0 and then make it a lot easier to set up (i.e. Docker, pip requirements.txt, etc)

For now, if you really really want to run it, you just have to bruteforce it - from the main project folder run python -m frontend.app (starts the backend), and in /royalty-automation/frontend/client run npm install then npm start (starts the frontend webpage). From there, there are very basic instructions on the webpage on how to use this sytem. 

You will also need a .env in the root folder with a PINECONE_API key and an OPENAI_KEY

# Discussion:

The way this project works is you upload a PDF -> pdf_extractor.py extracts the information -> extracted_data.json is generated -> data_cleaning.py is used to clean the data -> cleaned_data.pkl is generated and fed to -> extractor.py -> which pulls out the structure information in the form of combined_data.csv, and unstructured data in the form of output_data.json

# Limitations

There are a *lot* of limitations considering this is the barely functioning, minimal prototype! In the previous section you may have noticed that the filenames could be more clear (it'll be in Future Work I promise), the flask server gives this following warning when starting up: 

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

so this prototype definitely can't be used in production - however it is fine as it currently is. Another limitation is the fact that it can't handle multiple files at once, I eventually will make it so it can handle a directory or multiple files, but for now I just crossed the PoC phase with OpenAI v1.x.x. Another limitation is how I set up the database creation and handling, right now it creates one database and one database only, so unless there is a giant PDF with all of the information, it needs to be generalized better. 


# Future Work

TODO:
1. Fix response structures 

*vector_db: remove special characters/newline characters, return only text (not entire pinecone output)

*SQL: results aren't specific enough i.e. Alice Johnson Q1 query returns all author Q1 and 2 Q2 results 

2. Updating flask server to production grade
3. Certain naming conventions could be better
4. Maybe a little more modularity (i.e. extractor), I think I'm pretty modular, but there are a few cases one could argue for improvement
5. Embedding process in that it should allow for larger document sizes (chunking + cross chunk context preservation via a sentence or two overlapping)
6. Definitely need to work on how SQL tables are created and handled - this and #1 are most important I think (also ties into 3 a little bit, slightly redundant)
7. Fix the headers so they also get uploaded to SQL (right now there are none, so it is basically author name + values in the database)
8. Create auto data analysis functionality (farther down the line)
9. Make the UI a little nicer - it is okay as a prototype but I'd like it to be better
10. Unit testing
11. Way down the line add the ability for multiple calls to be placed

Once I fix the naming conventions, make the SQL/vector databases more generalized, update the flask server to production grade, round out the embedding process, along with a few other things I want to clean up (i.e. some functionality could be done better) I'll create the main.py file for easier program running, I'll set it up so that it is a lot easier to use after installing (talked about earlier in the beginning of the Setup section), and I'll provide more comprehensive instructions on how to use it! I'm happy with where it is at right now, but there is a lottttt that needs to be done

# Structure

This is more or less the overall structure - I may be missing a few files here and there, but I think this is a solid representation of the internal structure

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

