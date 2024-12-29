from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Top Songs page
@app.route('/Top Songs')
def top_songs():
    return render_template('top_songs.html')

# Route for the Top Artists page
@app.route('/Top Artists')
def top_artists():
    return render_template('top_artists.html')

# Route for the Top Genres page
@app.route('/Top Genres')
def top_genres():
    return render_template('top_genres.html')


if __name__ == '__main__':
    app.run(debug=True)