from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from db_storage import *
from song import Song
from playlist import Playlist

app = FastAPI()

class SongModel(BaseModel):
    title: str
    artist: str
    duration: int
    playcount: int = 0 #default value

class PlaylistModel(BaseModel):
    playlistName: str

class AddSongModel(BaseModel):
    song_id: int

@app.get("/")
def read_root():
    return {"message": "Welcome to Musify API", "version": "1.0"}

@app.get("/songs", response_model=List[SongModel])
def get_songs():
    songs = db_load_songs()
    return [song.song_to_dict() for song in songs]

@app.post("/songs")
def add_song(song: SongModel):# taking an object of SongModel class
    songOBJ = Song(song.title, song.artist, song.duration)#making a Song object using SongModel instance variables
    db_save_songs([songOBJ])#expects a list of songs
    return {"message": "Song added Successfully"}

@app.get("/playlists")
def get_playlist():
    playlists = db_load_playlists()
    return [{"id": playlist[0], "Name": playlist[1]} for playlist in playlists]

@app.post("/playlists")
def add_playlist(playlist: PlaylistModel): 
    db_create_playlist(playlist.playlistName)
    return {"message": "Playlist Created!"}

@app.post("/playlists/{playlist_id}/songs")
def add_song_to_playlist(playlist_id: int, data: AddSongModel):#takes data of AddSongModel class
    db_add_song_to_playlist(playlist_id, data.song_id)#takes song id from data object
    return {"message": "Song added to playlist"}