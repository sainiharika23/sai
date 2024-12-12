class Movies:
    def __init__(self, movie_name, song):
        self.movie_name = movie_name
        self.song = song

    def display_movie(self):
        print(f"The name of the movie is: {self.movie_name}")
        print(f"The song from the movie is: {self.song}")


class Director(Movies):
    def __init__(self, movie_name, song, hero):
        super().__init__(movie_name, song)
        self.hero = hero

    def display_director(self):
        print(f"The hero is: {self.hero}")


class Film(Director):
    def __init__(self, movie_name, song, hero, heroine):
        super().__init__(movie_name, song, hero)
        self.heroine = heroine

    def display_film(self):
        print(f"The heroine is: {self.heroine}")


# Input from the user
movie_name = input("Enter the name of the movie: ")
song = input("Enter the song name: ")
hero = input("Who is the hero?: ")
heroine = input("Who is the heroine?: ")

# Creating an object of Film
obj = Film(movie_name, song, hero, heroine)

# Displaying details
obj.display_movie()
obj.display_director()
obj.display_film()
