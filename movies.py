import json
import random
import movie_storage

MOVIES_FILE = "movies.json"


# def movie_storage.get_movies():
#     try:
#         with open(MOVIES_FILE, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}

# def movie_storage.save_movies(movies):
#     with open(MOVIES_FILE, "w") as f:
#         json.dump(movies, f, indent=4)


def get_movie_name():
    """ getting a movie name from the user """
    movie_name = input()
    # some input checks
    return movie_name


def get_movie_rating():
    """ getting a movie rating from the user """
    movie_rating = float(input())
    # some input checks
    return movie_rating


def list_movies(movies):
    """ printing out the list of movies and their amount """
    movies = movie_storage.get_movies()

    print(f"\n{len(movies)} movies in total")
    for movie, movie_info in movies.items():
        print(f"{movie} ({movie_info['year']}): {movie_info['rating']}")


def add_movie(movies):
    """ adding a new movie and its rating based on user input,
    using the previous functions """

    print("\nEnter new movie name: ")
    new_movie = get_movie_name()
    print("Enter new movie rating(0-10): ")
    new_movie_rating = get_movie_rating()
    year = int(input("Enter the release year: "))

    # movies[new_movie] = {"rating": new_movie_rating, "year": year}
    # movie_storage.save_movies(movies)

    movie_storage.add_movie(new_movie, new_movie_rating, year)

    print(f"Movie {new_movie} successfully added")


def delete_movie(movies):
    """ deleting a movie if it is in the database, based on user input """
    movies = movie_storage.get_movies()
    print("\nEnter movie to delete: ")
    movie_to_delete = get_movie_name()

    if movie_to_delete in movies:
        del movies[movie_to_delete]
        movie_storage.save_movies(movies)
        print(f"{movie_to_delete} deleted successfully")
    else:
        print(f"{movie_to_delete} does not exist in the database")


def update_movie(movies):
    """ updating the rating of a movie, if the movie is in the database, based on user input """
    movies = movie_storage.get_movies()
    print("\nEnter movie name: ")
    movie_to_update = get_movie_name()

    if movie_to_update in movies:
        new_rating = float(input(f"Enter the new rating for {movie_to_update}: "))
        movies[movie_to_update]["rating"] = new_rating
        movie_storage.save_movies(movies)
        print(f"The rating for {movie_to_update} was successfully updated")
    else:
        print(f"{movie_to_update} does not exist in the database")


def median_rating(movies):
    """ calculating the median of all the movie rating from the database """
    movies = movie_storage.get_movies()
    # rating_list = list(movies.values())
    rating_list = []

    for info in movies.values():
        rating = info["rating"]
        rating_list.append(rating)

    if not rating_list:
        return 0

    # sort the list to prepare for median calculation

    rating_list.sort()
    n = len(rating_list)
    middle = n // 2

    if n % 2 == 0:
        # Even number of ratings: average the two middle ones
        median = (rating_list[middle - 1] + rating_list[middle]) / 2
    else:
        # Odd number: take the middle one directly
        median = rating_list[middle]

    return median


def average_rating(movies):
    """ calculating the average of all the movie rating from the database """
    movies = movie_storage.get_movies()
    rating_list = []
    # rating_list = list(movies.values())

    for info in movies.values():
        rating = info["rating"]
        rating_list.append(rating)

    if not rating_list:
        return 0

    sum = 0
    for rating in rating_list:
        sum += rating

    average = sum / len(rating_list)
    return average


def best_rating(movies):
    """ identifying the best movie with the best rating """
    movies = movie_storage.get_movies()
    # rating_list = list(movies.values())
    best = 0
    for info in movies.values():
        rating = info["rating"]
        if rating > best:
            best = rating
    for movie, info in movies.items():
        if info["rating"] == best:
            print(f"Best movie: {movie}, {info["rating"]}")


def worst_rating(movies):
    """ identifying the worst movie with the best rating """
    movies = movie_storage.get_movies()
    # rating_list = list(movies.values())
    worst = 10
    for info in movies.values():
        rating = info["rating"]
        if rating < worst:
            worst = rating

    for movie, info in movies.items():
        if info["rating"] == worst:
            print(f"Worst movie: {movie}, {info["rating"]}")


def get_movie_stats(movies):
    """ getting all the required movies stats, using the previous functions """
    movies = movie_storage.get_movies()
    print(f"\nAverage rating: {average_rating(movies)}")
    print(f"Median rating: {median_rating(movies)}")
    best_rating(movies)
    worst_rating(movies)


def get_random_movie(movies):
    """ getting a random movie from the database """
    movies = movie_storage.get_movies()
    movies_and_ratings = list(movies.items())
    random_movie = random.choice(movies_and_ratings)
    print(
        f"\nYour movie for tonight: {random_movie[0]} ({random_movie[1]["year"]}), it's rated {random_movie[1]["rating"]}")


def search_movie(movies):
    """ searching for a movie in the database that matches the input fromm the user """
    # movies_list = list(movies.keys())
    movies = movie_storage.get_movies()
    title = input("\nEnter part of movie name: ")
    # for i in range(len(movies_list)):
    #     if title.lower() in movies_list[i].lower():
    #         print(f"\n{movies_list[i]}")
    for movie, info in movies.items():
        if title.lower() in movie.lower():
            print(f"{movie} ({info["year"]}), {info["rating"]}")


def sort_movies_desc(movies):
    """ sorting and listing the movies in descending order """
    # print("\n")
    movies = movie_storage.get_movies()
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
    for movie, info in sorted_movies:
        print(f"{movie} ({info["year"]}), {info["rating"]}")


def sort_movies_desc_year(movies):
    """ sorting and listing the movies in descending order """
    # print("\n")
    movies = movie_storage.get_movies()
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True)
    for movie, info in sorted_movies:
        print(f"{movie} ({info["year"]}), {info["rating"]}")


def print_menu():
    """ printing out the menu with options from which the user can choose """
    menu_text = """
    Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Movies sorted by year
    10. Filter movies
    """
    print(menu_text)


def user_menu_input(movies):
    """ executing the command from the menu that the user chose """
    movies = movie_storage.get_movies()
    while True:
        print_menu()
        user_input = input(f"Enter choice (0-10): ").strip()
        # Ignore empty input
        if not user_input:
            continue

        if user_input == "0":
            print("\nBye!")
            break

        if user_input == "1":
            list_movies(movies)
            input("\nPress enter to continue")

        elif user_input == "2":
            add_movie(movies)
            input("\nPress enter to continue")

        elif user_input == "3":
            delete_movie(movies)
            input("\nPress enter to continue")

        elif user_input == "4":
            update_movie(movies)
            input("\nPress enter to continue")

        elif user_input == "5":
            get_movie_stats(movies)
            input("\nPress enter to continue")

        elif user_input == "6":
            get_random_movie(movies)
            input("\nPress enter to continue")

        elif user_input == "7":
            search_movie(movies)
            input("\nPress enter to continue")

        elif user_input == "8":
            sort_movies_desc(movies)
            input("\nPress enter to continue")

        elif user_input == "9":
            sort_movies_desc_year(movies)
            input("\nPress enter to continue")

        # elif user_input == "9":
        #     create_rating_bar(movies)
        #     input("\nPress enter to continue")

        else:
            print(f"Invalid choice")
            continue


def main():
    print(10 * "*", "My Movies Database", 10 * "*")
    movies = movie_storage.get_movies()
    user_menu_input(movies)


if __name__ == "__main__":
    main()
