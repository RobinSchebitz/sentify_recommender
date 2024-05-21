import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import spotipy.util as util
import random

class CreatePlaylist:
    """
    A class for accessing your spotify account via the API using spotipy.
    Make sure to have a .env file prepared with your client id and client secret.
    Above you find an example use for using this class and the methods.

    Example usage:
    spotify_api = CreatePlaylist()
    my_playlist = spotify_api.create_playlist(name="TestAutomaticPlaylistGeneration", description="Automatically generated playlist")
    test_uri = ['spotify:track:7yyRTcZmCiyzzJlNzGC9Ol']
    spotify_api.add_tracks_to_playlist(my_playlist['id'], test_uri)

    """
    
    def __init__(self):

        load_dotenv()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("spotify_client_id"),
            client_secret=os.getenv("spotify_client_secret"),
            redirect_uri="http://localhost:8888/callback",
            scope='user-library-read playlist-modify-private',
            cache_path="token.txt"))




    def create_playlist(self, name, description, public=False):
        """ 
        A method from spotipy that creates an empty Spotify playlist for the account signed in via the API.
        It takes the playlist name and description and additional features (public and user_id)
        """
        results = self.sp.current_user()
        user_id = results['id']
        my_playlist = self.sp.user_playlist_create(user=f"{user_id}", name=name, public=public, description=description)
        return my_playlist
        

    def add_tracks_to_playlist(self, playlist_id, track_uris, position=None):
        """ 
        A method from spotipy that adds track to a Spotify playlist.
        Takes the playlist_id and a list of track URIs as arguments (and optionally the position of a track)
        """
        self.sp.playlist_add_items(playlist_id=playlist_id, items=track_uris, position=position)

    # Fetching Playlists from a User
    def fetch_playlists_user(self, user):

       
        username = str(user) #Take the username arg

        # Fetch Playlist Data from Spotify API
        playlists = self.sp.user_playlists(username, limit=5)

        # Return Playlist Information
        return playlists
    
    def fetch_tracks_from_playlist(self, playlist_id):

        track_uris = []

        #Fetch Tracks from playlist
        results = self.sp.playlist_items(playlist_id=playlist_id, limit=50)

        # Loop through each item in the response
        for item in results['items']:
            track = item['track']
            track_uris.append(track['uri'])

        return track_uris
