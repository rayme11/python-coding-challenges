# Write a function called average_rating that takes a dictionary movie_ratings as input.
# The dictionary contains movie names as keys and their corresponding ratings as values.
# The ratings are given on a scale of 1 to 5.
# Your task is to calculate and return the average rating for all the movies.
# for the sample below the output shall be 4.6

movie_ratings = {
    "The Shawshank Redemption": 5,
    "The Godfather": 4,
    "Pulp Fiction": 5,
    "The Dark Knight": 4,
    "Fight Club": 5
}


def average_rating(movies):
    avg_rating = 0
    for value in movies.values():
        print("The value is: ", value)
        avg_rating += value
    return avg_rating / len(movies)


print(average_rating(movie_ratings))
