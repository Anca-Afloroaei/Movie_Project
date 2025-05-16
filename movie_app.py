from colorama import Fore, init
import random
import requests

init(autoreset=True)   # resets the colors every time the program is run

OMDB_API_KEY = "396a519b"


class MovieApp:
    def __init__(self, storage):
        """This method initializes MovieApp with a storage backend."""
        self._storage = storage


    def list_movies(self):
        """This method lists all movies in the database."""
        movies = self._storage.list_movies()

        if "title" in movies.keys():
            print(Fore.GREEN + f"{len(movies)-1} movies in total")
        else:
            print(Fore.GREEN + f"{len(movies)} movies in total")
        for name, details in movies.items():
            if not name == "title":
                print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")

    def add_movie(self):
        """This method adds a new movie to the database."""
        movies = self._storage.list_movies()

        while True:
            name = input(Fore.YELLOW + "Enter movie name: ").strip()
            if not name:
                print(Fore.RED + "Movie name cannot be empty.")
            elif name in movies:
                print(Fore.YELLOW + f"{name} already exists.")
                return
            else:
                break


        try:
            url = f"http://www.omdbapi.com/?i=tt3896198&apikey={OMDB_API_KEY}&t={name}"
            response = requests.get(url)
            data = response.json()    # my movies.json file

            #title = data.get("Title", name)
            year = data.get("Year")
            rating = data.get("imdbRating")
            poster = data.get("Poster")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")


        # while True:
        #     try:
        #         rating = float(input(Fore.YELLOW + "Enter rating (1-10): "))
        #         if 1 <= rating <= 10:
        #             break
        #         else:
        #             print(Fore.RED + "Rating must be between 1 and 10.")
        #     except ValueError:
        #         print(Fore.RED + "Invalid input. Enter a number.")
        #
        # while True:
        #     try:
        #         year = int(input(Fore.YELLOW + "Enter release year: "))
        #         break
        #     except ValueError:
        #         print(Fore.RED + "Invalid input. Enter a valid year.")

        #title = data.get(name)




        #poster = "N/A"  # Placeholder, since your add_movie() requires it
        self._storage.add_movie(name, year, rating, poster)
        print(Fore.GREEN + f"{name} added successfully.")

    def delete_movie(self):
        """This method deletes a movie from the database."""
        name = input(Fore.YELLOW + "Enter movie name to delete: ").strip()
        movies = self._storage.list_movies()

        if name in movies:
            self._storage.delete_movie(name)
            print(Fore.GREEN + f"{name} deleted.")
        else:
            print(Fore.YELLOW + "Movie not found.")

    def update_movie(self):
        """This method updates an existing movie's rating."""
        name = input(Fore.YELLOW + "Enter movie name to update: ").strip()
        movies = self._storage.list_movies()

        if name not in movies:
            print(Fore.YELLOW + "Movie not found.")
            return

        while True:
            try:
                new_rating = float(input(Fore.YELLOW + "Enter new rating (1-10): "))
                if 1 <= new_rating <= 10:
                    break
                else:
                    print(Fore.RED + "Rating must be between 1 and 10.")
            except ValueError:
                print(Fore.RED + "Invalid input. Enter a number.")

        self._storage.update_movie(name, new_rating)
        print(Fore.GREEN + f"{name} updated successfully.")

    def movie_stats(self):
        """This method displays movie rating statistics."""
        movies = self._storage.list_movies()
        ratings = [details["rating"] for details in movies.values()]
        # ratings = []
        # for details in movies.values():
        #     ratings.append(details["rating"])
        if not ratings:
            print(Fore.YELLOW + "No movies in database.")
            return

        avg = round(sum(ratings) / len(ratings), 1)
        sorted_ratings = sorted(ratings)
        n = len(ratings)
        median = sorted_ratings[n // 2] if n % 2 else round((sorted_ratings[n // 2 - 1] + sorted_ratings[n // 2]) / 2, 1)
        max_rating = max(ratings)
        min_rating = min(ratings)

        best = [name for name, details in movies.items() if details["rating"] == max_rating]
        worst = [name for name, details in movies.items() if details["rating"] == min_rating]

        print(Fore.GREEN + f"Average rating: {avg}")
        print(Fore.GREEN + f"Median rating: {median}")
        print(Fore.GREEN + "Best rated movie(s):")
        for movie in best:
            print(Fore.BLUE + f"{movie}: {movies[movie]['rating']}")
        print(Fore.GREEN + "Worst rated movie(s):")
        for movie in worst:
            print(Fore.BLUE + f"{movie}: {movies[movie]['rating']}")

    def random_movie(self):
        """This method displays a randomly selected movie."""
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.YELLOW + "No movies available.")
            return
        name, details = random.choice(list(movies.items()))
        print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")

    def search_movie(self):
        """This method searches for movies by name."""
        query = input(Fore.YELLOW + "Enter movie name to search: ")
        movies = self._storage.list_movies()
        found = False
        for name, details in movies.items():
            if query.lower() in name.lower():
                print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")
                found = True
        if not found:
            print(Fore.YELLOW + "No matches found.")

    def sorted_by_rating(self):
        """This method displays movies sorted by rating descending."""
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
        print(Fore.GREEN + "Movies sorted by rating:")
        for name, details in sorted_movies:
            print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")

    def generate_website(self):
        """This method is a placeholder for website generation logic."""
        #print(Fore.YELLOW + "Website generation not yet implemented.")

        movies = self._storage.list_movies()

        try:
            with open("_static/index_template.html", "r", encoding="utf-8") as template_file:
                website_template = template_file.read()
        except FileNotFoundError:
            print(Fore.RED + "Website not found!")

        # container for output
        # loop through each movie in the json file - produce an html block

        movie_blocks = []

        # try:
        #     url = f"http://www.omdbapi.com/?i=tt3896198&apikey={OMDB_API_KEY}"
        #     response = requests.get(url)
        #     data = response.json()    # my movies.json file
        #
        #     title = data.get("Title")
        #     year = data.get("Year")
        #     poster = data.get("Poster")
        #
        # except Exception as e:
        #     print(Fore.RED + f"Error: {e}")


        for name, details in movies.items():
            try:
                url = f"http://www.omdbapi.com/?i=tt3896198&apikey={OMDB_API_KEY}&t={name}"
                response = requests.get(url)
                data = response.json()  # my movies.json file

                if data.get("Response") == "False":
                    print(Fore.RED + f"Movie not found in OMDb: {data.get('Error')}")
                    return

                title = data.get("Title", name)
                year = data.get("Year")
                poster = data.get("Poster")

            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Error accessing OMDb API: {e}")

            html_block = f"""
            <li>
                <div class="movie">
                    <img class="movie-poster" src="{poster}" alt="{title} poster"/>
                    <div class="movie-title">{title}</div>
                    <div class ="movie-year">{year}</div>
                </div>
            </li>
            """
            movie_blocks.append(html_block)

        all_movies_html = ""
        for block in movie_blocks:
            all_movies_html += block + "\n"

        final_template = website_template.replace("__TEMPLATE_MOVIE_GRID__", all_movies_html)

        try:
            with open("_static/index.html", "w", encoding="utf-8") as template_file:
                template_file.write(final_template)
            print(Fore.GREEN + "Website generated successfully")
        except Exception as e:
            print(Fore.RED + f"Website could not be generated: {e}")


        #print(Fore.YELLOW + "Website successfully generated")






    def run(self):
        """This method is the main program loop."""
        print(Fore.BLUE + "\n********** My Movies Database **********\n")

        while True:
            print(Fore.GREEN + "\nMenu:")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Show stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Sort by rating")
            print("9. Generate website")

            choice = input(Fore.YELLOW + "\nEnter your choice (0-9): ").strip()

            if choice == "0":
                print(Fore.GREEN + "Bye!")
                break
            elif choice == "1":
                self.list_movies()
            elif choice == "2":
                self.add_movie()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                self.update_movie()
            elif choice == "5":
                self.movie_stats()
            elif choice == "6":
                self.random_movie()
            elif choice == "7":
                self.search_movie()
            elif choice == "8":
                self.sorted_by_rating()
            elif choice == "9":
                self.generate_website()
            else:
                print(Fore.RED + "Invalid choice. Please enter a number between 0 and 9.")

            input(Fore.YELLOW + "\nPress Enter to continue...")