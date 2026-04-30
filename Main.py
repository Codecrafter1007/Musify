from storage import save_songs, load_songs
from song import Song
from Playlist import playlist
from User import user

#main

def menu():
    choice = True
    while (choice):
        print("Welcome to Musify!")
        print("1) Add a song")
        print("2) Create a playlist")
        print("3) Display library")
        print("4) Exit")
        
        user_input = int(input("Enter your Choice (1-4): "))
        
        match user_input:
                case 1:
                    addSong()
                case 3:
                    display_library()
                case 4:
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

def display_library():
    tempSongs = load_songs()
    if not tempSongs:
        print("LIBRARY IS EMPTY \n")
        
    else:
        for song in tempSongs:
            print(song.title)
menu()
