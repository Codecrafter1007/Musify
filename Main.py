from db_storage import *
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
        print("4) Display playlist")
        print("5) Display library")
        print("6) Exit")
        
        user_input = int(input("Enter your Choice (1-6): "))
        
        match user_input:
                case 1:
                    addSong()
                    print()
                case 2:
                    create_playlist()
                    print()
                case 3:
                    add_song_to_playlist()
                    print()
                case 4:
                    display_playlist()
                    print()
                case 5:
                    display_library()
                    print()
                case 6:
                    choice = False
                case _:
                    print("INVALID CHOICE! \n")       
def addSong():
    tempSongs = db_load_songs()
    
    title = input("Enter song name: ")
    artist = input("Enter artist's name: ")
    duration = int(input("Enter song duration: "))
    
    songObj = Song(title, artist, duration)
    tempSongs.append(songObj)
    db_save_songs(tempSongs)
    print(f"{title} added to library!")

def create_playlist():
    playlistName = input("Enter playlist name: ")
    db_create_playlist(playlistName)
    print("Playlist Created!")

def add_song_to_playlist():
    tempPlaylists = db_load_playlists()
    tempSongs = db_load_songs()
    
    for i in range(len(tempPlaylists)):
        print(f"#{i+1} {tempPlaylists[i][1]}")
        
    playlist_num = int(input("Choose playlist: "))
    playlist_name = tempPlaylists[playlist_num-1][1]
    
    for j in range(len(tempSongs)):
        print(f"#{j+1} {tempSongs[j].title}")
    
    song_num = int(input("Choose your song: "))
    song_name = tempSongs[song_num-1].title
    
    db_add_song_to_playlist(tempPlaylists[playlist_num-1][0], get_song_id(song_name))
    print(f"{song_name} added to {playlist_name}")

def display_playlist():
    tempPlaylist = db_load_playlists()
    if not tempPlaylist:
        print("NO PLAYLISTS")
    else:
        for i in range (len(tempPlaylist)):
            print(f"#{i+1} {tempPlaylist[i][1]}")

        playlist_num = int(input(("Choose playlist to display: ")))
        
        print()
        print(f"{tempPlaylist[playlist_num-1][1]}")
        print()
        
        songs = get_playlist_songs(get_playlist_id(tempPlaylist[playlist_num-1][1]))
        
        if not songs:
            print("No songs currently")
        else:
            for song in songs:
                print(f"{song[0]} by {song[1]}")
              

def display_library():
    tempSongs = db_load_songs()
    if not tempSongs:
        print("LIBRARY IS EMPTY \n")
        
    else:
        print()
        for song in tempSongs:
            print(f"{song.title} by {song.artist}")

menu()
