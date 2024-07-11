import requests
from flask import Flask, request, render_template

app = Flask(__name__)
api_key = "739a15e6"

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_data = None
    if request.method == 'POST':
        movie_title = request.form['title']
        url = f'http://www.omdbapi.com/?t={movie_title}&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            movie_data = response.json()
        else:
            movie_data = {'Error': 'Movie not found or an error occurred'}
    return render_template("index.html", movie=movie_data)

if __name__ == '__main__':
    app.run(debug=True)
