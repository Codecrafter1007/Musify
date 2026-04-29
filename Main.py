from storage import save_songs, load_songs
from song import Song
from Playlist import playlist
from User import user

#main
song1 = Song("Bulleya", "Papon", 357)
song2 = Song("Sach keh raha hai", "KK", 329)


# save
songs = [song1, song2]
save_songs(songs)

# load
loaded_songs = load_songs()
for song in loaded_songs:
    song.display()
    print(f"{song.playcount}")


