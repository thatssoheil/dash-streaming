from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

repo = {
    1: {
        'index': '1',
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'cover': '/static/the-shawshank-redemption.jpg',
        'director': 'Frank Darabont',
        'rating': '9.3',
        'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through '
                    'acts of common decency. '
    },
    2: {
        'index': '1',
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'cover': '/static/the-shawshank-redemption.jpg',
        'director': 'Frank Darabont',
        'rating': '9.3',
        'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through '
                    'acts of common decency. '
    },
    3: {
        'index': '1',
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'cover': '/static/the-shawshank-redemption.jpg',
        'director': 'Frank Darabont',
        'rating': '9.3',
        'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through '
                    'acts of common decency. '
    },
    4: {
        'index': '1',
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'cover': '/static/the-shawshank-redemption.jpg',
        'director': 'Frank Darabont',
        'rating': '9.3',
        'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through '
                    'acts of common decency. '
    },
    5: {
        'index': '1',
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'cover': '/static/the-shawshank-redemption.jpg',
        'director': 'Frank Darabont',
        'rating': '9.3',
        'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through '
                    'acts of common decency. '
    },
    6: {
        'index': '1',
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'cover': '/static/the-shawshank-redemption.jpg',
        'director': 'Frank Darabont',
        'rating': '9.3',
        'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through '
                    'acts of common decency. '
    }
}


@app.route('/')
@app.route('/index')
def home():
    data = repo
    return render_template('index.html', content=data)


@app.route('/movies/<int:number>')
def movie(number):
    data = repo.get(number)
    return render_template('movie.html', content=data)


if __name__ == '__main__':
    app.run()
