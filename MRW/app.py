from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from model import get_movie_list
from database import get_movie_title, get_movie_genres

app = Flask(__name__)



@app.route('/')
def hello_world():
    titles = get_movie_title()
    return render_template('index.html', titles=titles)


@app.route('/recommender', methods=['GET', 'POST'])
def recommender():
    movie_name = request.form['movie_name']
    recommenders = get_movie_list(movie_name)
    if len(recommenders) == 0:
        print(recommenders)
        return render_template('recommender.html', recommenders=['Sorry. I couldn\'t find any movie to recommend. '
                                                                 'I will improve myself on this.'])
    else:
        print(recommenders)
        return render_template('recommender.html', recommenders=recommenders)


if __name__ == '__main__':
    app.run()

