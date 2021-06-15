# The system was developed for movies with more than 1000 reviews.
def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
    rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts())
    rare_movies = comment_counts[comment_counts["title"] <= 1000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df


def item_based_recommender(movie_name):
    import pickle
    import pandas as pd
    user_movie_df = pickle.load(open('user_movie_df.pkl', 'rb'))
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(6)


def get_movie_list(movie_name):
    movies_form_item_based = item_based_recommender(movie_name)
    return movies_form_item_based[1:6].index

