import psycopg2
from dotenv import load_dotenv
import os

load_dotenv() #reads the .env file

conn = psycopg2.connect(
    host = "localhost",
    database = "musify",
    user = "postgres",
    password = os.getenv("DB_PASSWORD")   #reads passwords from .env
)

print("Connected Successfully!")
conn.close()