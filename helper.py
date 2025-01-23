from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv


# imports environment variables_ such as keys
load_dotenv()

scope = "user-top-read"

user_sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
client_sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())



# get the top songs for each time range
def get_top_songs_short():
    top_songs = user_sp.current_user_top_tracks(limit=50, time_range='short_term')
    d = [None] * 50
    
    for i, item in enumerate(top_songs['items']):
        d[i] = item
        
    return d

def get_top_songs_medium():
    top_songs = user_sp.current_user_top_tracks(limit=50, time_range='medium_term')
    d = [None] * 50
    
    for i, item in enumerate(top_songs['items']):
        d[i] = item
        
    return d

def get_top_songs_long():
    top_songs = user_sp.current_user_top_tracks(limit=50, time_range='long_term')
    d = [None] * 50
    
    for i, item in enumerate(top_songs['items']):
        d[i] = item
        
    return d



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

# get the top artists for each time range 
def get_top_artists_short():     
    top_artists = user_sp.current_user_top_artists(limit=50, time_range='short_term')
    d = [None] * 50
    
    for i, item in enumerate(top_artists['items']):
        d[i] = item
        
    return d

def get_top_artists_medium():
    top_artists = user_sp.current_user_top_artists(limit=50, time_range='medium_term')
    d = [None] * 50
    
    for i, item in enumerate(top_artists['items']):
        d[i] = item
        
    return d

def get_top_artists_long():
    top_artists = user_sp.current_user_top_artists(limit=50, time_range='long_term')
    d = [None] * 50
    
    for i, item in enumerate(top_artists['items']):
        d[i] = item
        
    return d

# get the top genres for each time range
def get_top_genres_short():
    #take last 50 songs and get the genres of the artists
    #count the amount of times each genre appears and return the top 5
    top_songs = user_sp.current_user_top_tracks(limit=50, time_range='short_term')
    d = []
    for item in top_songs['items']:
        artist = item['artists'][0]['id']
        artist_info = client_sp.artist(artist)
        for genre in artist_info['genres']:
            if genre in d:
                d[genre] += 1
            else:
                d[genre] = 1
                
                
                
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_dict.keys())[:5]

def get_top_genres_medium():
    #take last 50 songs and get the genres of the artists
    #count the amount of times each genre appears and return the top 5
    top_songs = user_sp.current_user_top_tracks(limit=50, time_range='medium_term')
    d = []
    for item in top_songs['items']:
        artist = item['artists'][0]['id']
        artist_info = client_sp.artist(artist)
        for genre in artist_info['genres']:
            if genre in d:
                d[genre] += 1
            else:
                d[genre] = 1
                
def get_top_genres_long():
    #take last 50 songs and get the genres of the artists
    #count the amount of times each genre appears and return the top 5
    top_songs = user_sp.current_user_top_tracks(limit=50, time_range='long_term')
    d = []
    for item in top_songs['items']:
        artist = item['artists'][0]['id']
        artist_info = client_sp.artist(artist)
        for genre in artist_info['genres']:
            if genre in d:
                d[genre] += 1
            else:
                d[genre] = 1
                

