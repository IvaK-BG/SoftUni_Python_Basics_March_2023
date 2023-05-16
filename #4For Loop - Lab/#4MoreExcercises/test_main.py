count_movies = int(input())
high_movie_name = ""
high_movie_rating = - 10

low_movie_name = ""
low_movie_rating = 10

average_rating = 0

for _ in range(count_movies):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > high_movie_rating:
        high_movie_name = movie_name
        high_movie_rating = movie_rating

    elif movie_rating < low_movie_rating:
        low_movie_name = movie_name
        low_movie_rating = movie_rating

    average_rating += movie_rating

print(f"{high_movie_name} is with highest rating: {high_movie_rating:.1f}")
print(f"{low_movie_name} is with lowest rating: {low_movie_rating:.1f}")
print(f"Average rating: {average_rating/count_movies:.1f}")