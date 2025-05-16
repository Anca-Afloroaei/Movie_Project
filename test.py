from movie_app import MovieApp
from storage.storage_csv import StorageCsv

storage = StorageCsv('movies.csv')
movie_app = MovieApp(storage)
movie_app.run()



# from storage_json import StorageJson
#
# storage = StorageJson('movies.json')
# print(storage.list_movies())
#
# storage.add_movie("Enchanted", 2024, 10)
# print(storage.list_movies())
