from flask import Flask, render_template
import helper

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Top Songs page
@app.route('/top_songs')
def top_songs():
    short_term_tracks = helper.get_top_songs_short()
    medium_term_tracks = helper.get_top_songs_medium()
    long_term_tracks = helper.get_top_songs_long()
    return render_template('top_songs.html', short_term_tracks=short_term_tracks, medium_term_tracks=medium_term_tracks, long_term_tracks=long_term_tracks)

# Route for the Top Artists page
@app.route('/top-artists')
def top_artists():
    return render_template('top_artists.html')

# Route for the Top Genres page
@app.route('/top-genres')
def top_genres():
    return render_template('top_genres.html')


if __name__ == '__main__':
    app.run(debug=True)