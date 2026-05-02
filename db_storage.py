import psycopg2
import os
from dotenv import load_dotenv
from song import Song
from Playlist import playlist
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

def db_create_playlist(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO playlists(name) VALUES(%s)", (name,))
    conn.commit()
    conn.close()
    
def db_load_playlists():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM playlists")
    rows = cursor.fetchall() #fetches entire data from the table
    conn.close()
    return rows

def db_add_song_to_playlist(playlist_id, song_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO playlist_songs (playlist_id, song_id) VALUES(%s, %s)", (playlist_id, song_id))
    conn.commit()
    conn.close()
    
def get_playlist_id(playlist_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM playlists WHERE name = %s", (playlist_name,))
    id = cursor.fetchone()
    id = id[0]
    conn.close()
    return id

def get_song_id(song_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM songs WHERE title = %s", (song_name,))
    id = cursor.fetchone()
    id = id[0]
    conn.close()
    return id

def get_playlist_songs(playlist_id):
    conn = get_connection()
    cursor  = conn.cursor()
    cursor.execute("SELECT songs.title, songs.artist FROM songs JOIN playlist_songs ON songs.id = playlist_songs.song_id WHERE playlist_songs.playlist_id = %s", (playlist_id,))
    songs = cursor.fetchall()
    return songs