import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def create_leads_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id SERIAL PRIMARY KEY,
            name TEXT,
            role TEXT,
            email TEXT,
            company TEXT,
            source TEXT,
            linkedin TEXT,
            instagram TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
