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
    
    def song_to_dict(self):
        return {"title":self.title,
                "artist":self.artist,
                "duration":self.duration,
                "playcount":self.playcount}

    @classmethod
    def song_from_dict(cls, data):
        song = cls(data["title"], data["artist"], data["duration"])
        song.playcount = data["playcount"]
        return (song)