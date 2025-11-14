def calculate_roi(movie_tuple):
    movie_id, genre, budget, revenue = movie_tuple
     return revenue / budget


def find_most_profitable_movie(movies):
 sorted_movies = sorted(movies, key=lambda m:
         (-calculate_roi(m), m[0]))
    return sorted_movies[0][0]


def get_movies_in_genre(movies, genre_name):
    genre_list = [m[0] for m in movies if m[1] == genre_name]
    return sorted(genre_list)


def get_genre_revenue_summary(movies):
    genre_dict = {}

    for movie_id, genre, budget, revenue in movies:
        genre_dict[genre] = genre_dict.get(genre, 0) + revenue
    summary = list(genre_dict.items())
    return sorted(summary, key=lambda x: x[0])


def analyze_movie_data(movies):
    most_profitable = find_most_profitable_movie(movies)
    sci_fi_movies = get_movies_in_genre(movies, 'Sci-Fi')
    genre_summary = get_genre_revenue_summary(movies)

    return (most_profitable, sci_fi_movies, genre_summary) 