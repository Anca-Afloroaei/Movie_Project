import json

from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path


    def list_movies(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


    def add_movie(self, title, year, rating, poster):
        pass

    def delete_movie(self, title):
        pass

    def update_movie(self, title, rating):
        pass



test_movies = StorageJson("movies.json")
print(test_movies.list_movies())























    # def list_movies(self):
    #     with open(self.file_path, "r", encoding="utf-8") as handle:
    #         movies = json.load(handle)
    #     return movies
    #
    # def add_movie(self, title, year, rating, poster):
    #     """ not sure if it's correct """
    #     movies = self.list_movies()
    #     movies[title].update({"year": year, "rating": rating, "poster": poster})
    #     with open(self.file_path, "w", encoding="utf-8") as handle:
    #         json.dump(movies, handle, indent=4)
    #
    #
    # def delete_movie(self, title):
    #     """ not sure if it's correct """
    #     movies = self.list_movies()
    #     del movies[title]
    #     with open(self.file_path, "w", encoding="utf-8") as handle:
    #         json.dump(movies, handle, indent=4)
    #
    # def update_movie(self, title, rating):
    #     """ not sure if it's correct """
    #     movies = self.list_movies()
    #     movies[title]["rating"] = rating
    #     with open(self.file_path, "w", encoding="utf-8") as handle:
    #         json.dump(movies, handle, indent=4)