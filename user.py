from Playlist import playlist
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