from storage_json import StorageJson
from movie_app import MovieApp

def main():
    """ initializing the movie app with JSON storage and starting the main loop """
    storage = StorageJson("movies.json")  # RELATIVE path to file
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()