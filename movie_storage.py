import json

MOVIES_FILE = "movies.json"


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open(MOVIES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_movies(movies):
    """
        Gets all movies as an argument and saves them to the JSON file.
    """
    with open(MOVIES_FILE, "w") as f:
        json.dump(movies, f, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_list = get_movies()
    movies_list[title] = {"year": year, "rating": rating}
    save_movies(movies_list)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_list = get_movies()
    if title in movies_list:
        del movies_list[title]
        save_movies(movies_list)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_list = get_movies()

    if title in movies_list:
        movies_list[title]["rating"] = rating
        save_movies(movies_list)

