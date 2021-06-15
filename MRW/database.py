def connect_db():
    from sqlalchemy import create_engine
    import mysql.connector

    #  The database was used to pull the movie titles.
    creds = {'user': '',
             'passwd': '',
             'host': '',
             'port': '',
             'db': ''
             }

    # MySQL conection string.
    connstr = 'mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}'
    return create_engine(connstr.format(**creds))


def get_movie_title():
    import pandas as pd
    conn = connect_db()
    result = pd.read_sql_query("select title from movie", conn)
    titles = result['title'].values
    return titles



def get_movie_genres():
    import pandas as pd
    conn = connect_db()
    return pd.read_sql_query("select genres from movie", conn)
