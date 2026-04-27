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

#main
song1 = Song("Bulleya", "Papon", 357)
song2 = Song("Sach keh raha hai", "KK", 329)

song1.play()
print(song1.getPlaycount())  # will print 1, not 0