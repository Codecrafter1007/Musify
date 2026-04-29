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