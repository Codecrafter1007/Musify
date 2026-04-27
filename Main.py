class Song:
    
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.playcount = 0
    
    def display(self):
        print(f"{self.title} by {self.artist} \n")
    
    def play(self):
        self.playcount +=1
        print("Now playing ")
        self.display()
    
    def getPlaycount(self):
        return self.playcount

class playlist:
    def __init__(self, playlistName):
        self.playlistName = playlistName
        self._songs = []
        self.songcount = 0
    
    def addSong(self, song):
        self._songs.append(song)
        self.songcount += 1
        print(f"{song.title} added! \n")
    
    def display(self):
        print(f"-------------{self.playlistName}-------------\n")
        
        for i in self._songs:
            i.display()

class user:
    
    def __init__(self, userName):
        self.userName = userName
        self.playlistCount = 0
        self._playlists = []

    def addPlaylist(self, playlist):
        self._playlists.append(playlist)
                
    def createPlaylist(self, playlistName):
        playlistName = playlist(playlistName)
        self.addPlaylist(playlistName)
        print("Playlist created! \n")
    
    def add_song_to_playlist(self, playlist_number, song):
        self._playlists[playlist_number - 1].addSong(song)
        
    
    def display(self):
        print(f"***************{self.userName}****************\n")

        for i in self._playlists:
            i.display()
        
    
    
#main
song1 = Song("Bulleya", "Papon", 357)
song2 = Song("Sach keh raha hai", "KK", 329)

user1 = user("Amish")
user1.createPlaylist("sad songs")
user1.add_song_to_playlist(1, song1)
user1.add_song_to_playlist(1, song2)
user1.display()

