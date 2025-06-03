import psycopg2
from psycopg2 import OperationalError

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="tradesync",
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432"
        )
        return conn
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
        raise
