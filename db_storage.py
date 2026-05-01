import psycopg2
import os
from dotenv import load_dotenv
from song import Song
load_dotenv()

def get_connection():
    return psycopg2.connect(
        host = "localhost",
        database = "musify",
        user = "postgres",
        password = os.getenv("DB_PASSWORD")
    )

def db_load_songs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM songs")
    rows = cursor.fetchall() #fetches entire data from the table
    conn.close()
    
    songs = []
    for row in rows:
        song = Song(row[1], row[2], row[3])
        song.playcount = row[4]
        songs.append(song)
    return songs

def db_save_songs(songs):
    conn = get_connection()
    cursor = conn.cursor()
    
    for song in songs:
        cursor.execute("INSERT INTO songs(title, artist , duration , playcount) VALUES(%s , %s , %s , %s) ON CONFLICT (title) DO NOTHING;",
                       (song.title, song.artist, song.duration, song.playcount))
        
    conn.commit()
    conn.close()
songs = db_load_songs()
db_save_songs(songs)