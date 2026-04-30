from storage import save_songs, load_songs, save_playlists,load_playlists
from song import Song
from Playlist import playlist
from User import user

#main

def menu():
    choice = True
    while (choice):
        print("Welcome to Musify!")
        print("1) Add song to library")
        print("2) Create a playlist")
        print("3) Add song to playlist")
        print("4) Display library")
        print("5) Exit")
        
        user_input = int(input("Enter your Choice (1-4): "))
        
        match user_input:
                case 1:
                    addSong()
                case 2:
                    create_playlist()
                case 3:
                    add_song_to_playlist()
                case 4:
                    display_library()
                case 5:
                    choice = False
                case _:
                    print("INVALID CHOICE! \n")       
def addSong():
    tempSongs = load_songs()
    
    title = input("Enter song name: ")
    artist = input("Enter artist's name: ")
    duration = int(input("Enter song duration: "))
    
    songObj = Song(title, artist, duration)
    tempSongs.append(songObj)
    save_songs(tempSongs)

def create_playlist():
    tempPlaylists = load_playlists()
    playlistName = input("Enter playlist name: ")
    playlistobj = playlist(playlistName)
    tempPlaylists.append(playlistobj)
    save_playlists(tempPlaylists)

def add_song_to_playlist():
    tempPlaylists = load_playlists()
    tempSongs = load_songs()
    
    for i in range(len(tempPlaylists)):
        print(f"#{i+1} {tempPlaylists[i].playlistName}")
        
    playlist_num = int(input("Choose playlist: "))
    
    for j in range(len(tempSongs)):
        print(f"#{j+1} {tempSongs[j].title}")
    
    song_num = int(input("Choose your song: "))
    
    tempPlaylists[playlist_num-1].addSong(tempSongs[song_num-1])
    
    save_playlists(tempPlaylists)

def display_library():
    tempSongs = load_songs()
    if not tempSongs:
        print("LIBRARY IS EMPTY \n")
        
    else:
        for song in tempSongs:
            print(f"{song.title} by {song.artist}")

menu()
