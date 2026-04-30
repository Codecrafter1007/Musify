from song import Song
from Playlist import playlist
import json

#for songs
songs_file_path = "D:/VSCode/musify/library.json"
def save_songs(songs):
    data = [song.song_to_dict() for song in songs]


    with open(songs_file_path, 'w') as file:
        json.dump(data, file)
        print(f"Data saved in '{songs_file_path}'")

def load_songs():
    try:
        with open(songs_file_path, 'r') as file:
            data = json.load(file)
            
            songs = []
            for i in data:
                song = Song.song_from_dict(i)
                songs.append(song) 
            return songs
        
    except FileNotFoundError:
        print("NO DATA FOUND!")
        return []
    except json.JSONDecodeError:
        return []
    
#for playlists
playlists_file_path = "D:/VSCode/musify/playlists.json"
def save_playlists(playlists):
    data = [pl.pl_to_dict() for pl in playlists]


    with open(playlists_file_path, 'w') as file:
        json.dump(data, file)
        print(f"Data saved in '{playlists_file_path}'")

def load_playlists():
    try:
        with open(playlists_file_path, 'r') as file:
            data = json.load(file)
            
            playlists = []
            for i in data:
                playlistobj = playlist.pl_from_dict(i)
                playlists.append(playlistobj) 
            return playlists
        
    except FileNotFoundError:
        print("NO DATA FOUND!")
        return []
    except json.JSONDecodeError:
        return []