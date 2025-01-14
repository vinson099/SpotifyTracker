from flask import Flask, render_template
import helper

app = Flask(__name__)

# Currently being placeheld by the top songs page
# # Route for the home page
# @app.route('/')
# def home():
#     return render_template('home.html', short_term_tracks = helper.get_top_songs_short())


@app.route('/')
def home():
    short_term_tracks = helper.get_top_songs_short()
    medium_term_tracks = helper.get_top_songs_medium()
    long_term_tracks = helper.get_top_songs_long()
    return render_template('top_songs.html', 
                           short_term_tracks=short_term_tracks, 
                           medium_term_tracks=medium_term_tracks, 
                           long_term_tracks=long_term_tracks)


# Route for the Top Songs page
@app.route('/top_songs')
def top_songs():
    short_term_tracks = helper.get_top_songs_short()
    medium_term_tracks = helper.get_top_songs_medium()
    long_term_tracks = helper.get_top_songs_long()
    return render_template('top_songs.html', 
                           short_term_tracks=short_term_tracks, 
                           medium_term_tracks=medium_term_tracks, 
                           long_term_tracks=long_term_tracks)

# Route for the Top Artists page
@app.route('/top_artists')
def top_artists():
    short_term_artists = helper.get_top_artists_short()
    medium_term_artists = helper.get_top_artists_medium()
    long_term_artists = helper.get_top_artists_long()
    return render_template('top_artists.html', 
                           short_term_artists=short_term_artists, 
                           medium_term_artists=medium_term_artists, 
                           long_term_artists=long_term_artists)

# Route for the Top Genres page
@app.route('/top-genres')
def top_genres():
    return render_template('top_genres.html')

#template to convert spotipy's duration to minutes and seconds
@app.template_filter('format_duration')
def format_duration(duration_ms):
    minutes = duration_ms // 60000
    seconds = (duration_ms // 1000) % 60
    return f"{minutes}:{seconds:02d}"

if __name__ == '__main__':
    app.run(debug=True)