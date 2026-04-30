from song import Song

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
        
    def pl_to_dict(self):
        _dictSongs = [song.song_to_dict() for song in self._songs]
        
        dict_Paylist = {"Playlist Name" : self.playlistName, "songs" : _dictSongs}  
        return dict_Paylist
    
    @classmethod
    def pl_from_dict(cls, data):
        Playlist = cls(data["Playlist Name"])
        
        for songdict in data["songs"]:
            Playlist._songs.append(Song.song_from_dict(songdict)) 

        return Playlist