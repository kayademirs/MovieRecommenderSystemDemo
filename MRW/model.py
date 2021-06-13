def item_based_recommender(movie_name):
    import pickle
    import pandas as pd
    user_movie_df = pickle.load(open('user_movie_df.pkl', 'rb'))
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(6)


def get_movie_list(movie_name):
    movies_form_item_based = item_based_recommender(movie_name)
    return movies_form_item_based[1:6].index

