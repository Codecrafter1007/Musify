from song import Song
import json

file_path = "D:/VSCode/musify/library.json"
def save_songs(songs):
    data = [song.to_dict() for song in songs]


    with open(file_path, 'w') as file:
        json.dump(data, file)
        print(f"Data saved in '{file_path}'")

def load_songs():
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            songs = []
            for i in data:
                song = Song.from_dict(i)
                songs.append(song) 
            return songs
        
    except FileNotFoundError:
        print("NO DATA FOUND!")
        return []
    except json.JSONDecodeError:
        print("LIBRARY IS EMPTY")
        return []