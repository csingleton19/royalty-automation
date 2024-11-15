import sqlite3
import os
import pandas as pd

# Define paths to the database and CSV file
DB_PATH = os.path.join("database", "data.db")
CSV_PATH = os.path.join("storage", "csv", "combined_data.csv")
TABLE_NAME = "combined_data"

def initialize_database():
    """Create a connection to the SQLite database, creating the file if it doesn't exist."""
    # Check if the database file already exists
    if not os.path.exists(DB_PATH):
        # Connect to the SQLite database (will create the file if it doesn't exist)
        with sqlite3.connect(DB_PATH) as conn:
            print("Database created successfully.")
    else:
        print("Database already exists. No action taken.")

def check_table_exists(cursor, table_name):
    """Check if the table exists in the database."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return bool(cursor.fetchone())

def load_data_into_database():
    """Load CSV data into the SQLite database, checking for table and data existence."""
    # Load the CSV data into a DataFrame
    data = pd.read_csv(CSV_PATH)

    # Connect to the SQLite3 database
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Check if the table already exists
        if not check_table_exists(cursor, TABLE_NAME):
            # If not, create the table and insert the data
            data.to_sql(TABLE_NAME, conn, index=False)
            print(f"Data loaded successfully into {TABLE_NAME} table.")
        else:
            # Check if the table has data
            cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
            row_count = cursor.fetchone()[0]
            if row_count == 0:
                data.to_sql(TABLE_NAME, conn, index=False, if_exists='replace')
                print(f"Data loaded successfully into {TABLE_NAME} table.")
            else:
                print("Data already exists in the database. No data loaded.")

if __name__ == "__main__":
    # Initialize database and load data
    initialize_database()
    load_data_into_database()

