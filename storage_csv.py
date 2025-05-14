import csv
import os
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        """ initializing the class """
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.writelines("title, rating, year")


    def _load_movies(self):
        """This helper method loads all movies from the file into a dictionary."""
        movies = {}
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    title, rating, year = parts
                    movies[title] = {
                        "rating": rating,
                        "year": year
                    }
        return movies

    def _save_movies(self, movies):
        """This helper method saves the entire movie dictionary to the file."""
        with open(self.file_path, "w") as file:
            for title, data in movies.items():
                file.write(f"{title},{data['rating']},{data['year']}\n")

    def list_movies(self):
        """This method returns all movies as a dictionary."""
        return self._load_movies()


    def add_movie(self, title, year, rating, poster=None):
        """ adding a new movie and its rating based on user input,
        using the previous functions """

        movies_list = self._load_movies()
        movies_list[title] = {"rating": rating, "year": year}
        self._save_movies(movies_list)


    def delete_movie(self, title):
        """" docstring """

        movies_list = self._load_movies()
        if title in movies_list:
            del movies_list[title]
            self._save_movies(movies_list)


    def update_movie(self, title, rating):
        """" docstring """

        movies_list = self._load_movies()
        if title in movies_list:
            movies_list[title]["rating"] = rating
            self._save_movies(movies_list)



    # def _load_movies(self):
    #     """This function loads and returns the movie data from the JSON file."""
    #     try:
    #         with open(self.file_path, "r") as f:
    #             return json.load(f)
    #     except FileNotFoundError:
    #         return {}

    # def _save_movies(self):
    #     """Gets all movies as an argument and saves them to the CSV file. """
    #     with open(self.file_path, "w") as f:
    #         f.writelines()
    #
    #         json.dump(self, f, indent=4)
    #
    #
    # def list_movies(self):
    #     """ printing out the list of movies and their amount """
    #     #return self._load_movies()    # private helper method _load_movies() includes the try/except
    #     try:
    #         with open(self.file_path, "r") as f:
    #             return json.load(f)
    #     except FileNotFoundError:
    #         return {}


    # def add_movie(self, title, year, rating, poster):
    #     """ adding a new movie and its rating based on user input,
    #     using the previous functions """
    #
    #     movies_list = self.list_movies()
    #     movies_list[title] = {"year": year, "rating": rating}
    #     self._save_movies(movies_list)



    # def delete_movie(self, title):
    #
    #
    #     movies_list = self.list_movies()
    #     if title in movies_list:
    #         del movies_list[title]
    #         self._save_movies(movies_list)



    # def update_movie(self, title, rating):
    #
    #
    #     movies_list = self.list_movies()
    #     if title in movies_list:
    #         movies_list[title]["rating"] = rating
    #         self._save_movies(movies_list)





# test_movies = StorageJson("movies.json")
# print(test_movies.get_movies())























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