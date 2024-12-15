import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv


# imports environment variables
load_dotenv()

scope = "user-top-read"

user_sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
client_sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())




def get_top_songs():
    top_songs = user_sp.current_user_top_tracks(limit=10, time_range='short_term')
    d = {}
    for i, item in enumerate(top_songs['items']):
        d[i+1] = item['name']
    return d


def get_top_artists():
    # returns a dictionary in the form of 
        # items:
        #     external_urls: uri of the artist
        #     followers: number of followers
        #     genres: list of genres
        #     href: link to the artist -> Use this to retrieve details about the artist, like followers, 
        #           genres, popularity, and associated albums.
        #     id: id of the artist
        #     images: list of images at different resolutions
        #     name: name of the artist
        #     popularity: popularity score of the artist (0-100)
        #     type: type of object (artist)
        #     uri: uri of the artist
            
    top_artists = user_sp.current_user_top_artists(limit=10, time_range='short_term')
    for i, item in enumerate(top_artists['items']):
        print(f"{i+1}: {item['name']}")
    
    
# print(get_top_songs())
print(get_top_artists())