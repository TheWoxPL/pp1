class MusicPiece:
    def __init__(self, artist, title, album, year):
        self.artist=artist
        self.title=title
        self.album=album
        self.year=year

    def __str__(self):
        return f"Performer:\t{self.artist}\nSong:\t\t{self.title}\nAlbum:\t\t{self.album}\nYear:\t\t{self.year}\n"

obj1=MusicPiece("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
print(obj1)
obj2=MusicPiece("James", "RandomTitle", "Album", 1999)
print(obj2)
obj3=MusicPiece("John", "RandomTitle", "Album", 1999)
print(obj3)