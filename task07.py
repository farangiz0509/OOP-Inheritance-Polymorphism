class Media:
    def __init__(self, title, author):
        self.title = title 
        self.author = author

    def play(self):
        raise NotImplementedError("Bunday metod yo'q!")
    

class Song(Media):
    def play(self):
        return f"Qo'shiq: {self.title}, Muallifi: {self.author}"

class Movie(Media):
    def play(self):
        return f"Film: {self.title}, Muallifi: {self.author}"

class Podcast(Media):
    def play(self):
        return f"Raqamli audio: {self.title},  Muallifi: {self.author}"


song = Song("Oq bulutlar","Jahongir Otajonov")
movie = Movie("Jannat onalar oyog'i ostida", "Shodmonova Jumagul")
podcast = Podcast("Texnologiya va Kelajak", "Ergasheva Tozagul")


print("Song:", song.play())
print("Movie:", movie.play())
print("Podcast:", podcast.pl)