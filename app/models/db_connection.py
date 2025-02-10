import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection function
def create_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def execute_query(query, params=None):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)  # Secure parameterization
            # Fetch all rows
            result = cursor.fetchall()

            # Get column names from cursor description
            columns = [desc[0] for desc in cursor.description]

            # Convert to DataFrame
            df = pd.DataFrame(result, columns=columns)
            return df
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        conn.close()
