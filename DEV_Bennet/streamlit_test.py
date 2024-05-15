import streamlit as st
import pandas as pd
import numpy as np

from CreatePlaylist import CreatePlaylist

import pandas as pd
import json
import scipy as sp
import numpy as np


# Load JSON data from file
with open('../data/challenge_set.json', 'r') as file: # Replace with local dataset path
    data = json.load(file)

# Initialize an empty list to collect all track data
all_tracks = []

# Loop through each playlist in the dataset
for playlist in data['playlists']:
    for track in playlist['tracks']:
        # Add playlist-level information to each track record
        track_info = {
            'playlist_name': playlist.get('name', 'Unknown'),
            'playlist_pid': playlist['pid'],
            'playlist_num_tracks': playlist['num_tracks'],
            'track_pos': track['pos'],
            'artist_name': track['artist_name'],
            'track_uri': track['track_uri'],
            'artist_uri': track['artist_uri'],
            'track_name': track['track_name'],
            'album_uri': track['album_uri'],
            'duration_ms': track['duration_ms'],
            'album_name': track['album_name']
        }
        all_tracks.append(track_info)

# Convert the list of track dictionaries to a DataFrame
df_spotify = pd.DataFrame(all_tracks)

sim_matrix_test = sp.sparse.load_npz('sparse_matrix.npz')
sim_matrix_df = pd.DataFrame.sparse.from_spmatrix(sim_matrix_test)

# Build index with track uris
track_uri = df_spotify['track_uri']
indices = pd.Series(df_spotify.index, index=df_spotify['track_uri'])

# Function that get track recommendations based on the cosine similarity 
def track_recommendations(track):

    #get the index of the track we put into the function
    idx = indices[track].iloc[0]

    #calculate all cosine similarities to that track and store it in a list
    sim_scores = list(enumerate(sim_matrix_df[idx]))

    #sort the list staring with the highest similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:100]

    #get the indeces of that 1000 tracks
    track_indices = [i[0] for i in sim_scores]

    recommended_tracks = track_uri.iloc[track_indices].drop_duplicates(keep='first').iloc[1:4]
    return recommended_tracks

# Building an interface
st.title('Sentify Song Recommender')

user_input = st.text_input('Enter your favorite song:')

if st.button('Recommend'):
    # Replace the following with your model's prediction logic
    recommendations = track_recommendations(user_input)  
    st.write('Recommended Songs:', recommendations)


""" spotify_api = CreatePlaylist()
my_playlist = spotify_api.create_playlist(name="Streamlit-test", description="Automatically generated playlist")
test_uri = recommendations
spotify_api.add_tracks_to_playlist(my_playlist['id'], test_uri) """


