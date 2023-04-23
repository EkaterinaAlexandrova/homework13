import os


class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating, year,
                 budget, box_office, profitable, oscar_nominated, oscar_win, trailer):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer = trailer
        self.storage_address = ""

    def play_trailer(self):
        print(f"Now playing trailer for {self.title}: {self.trailer}")

    def get_cast_list(self):
        return ", ".join(self.cast)

    def upload_file(self):
        directory = self.title[0].upper()
        filename = f"{self.title.replace(' ', '_')}.txt"
        file_path = os.path.join(os.getcwd(), "film_player", "film_storage", directory, filename)
        with open(file_path, "w") as file:
            file.write(self.description)
        self.storage_address = file_path

    def get_film_address(self):
        if not self.storage_address:
            return "File not uploaded yet."
        return self.storage_address
