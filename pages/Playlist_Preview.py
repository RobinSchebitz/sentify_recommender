import streamlit as st
from CreatePlaylist import CreatePlaylist
import pandas as pd
import json
import scipy as sp
import time

def run():

    # Load JSON data from file
    with open('data/challenge_set.json', 'r') as file: # Replace with local dataset path
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

    sim_matrix_test = sp.sparse.load_npz('models/sparse_matrix.npz')
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
    
    # Function to get the recommendations for a whole playlist
    def playlist_recommendations(playlist_id):

        # Instantiate a CreatePlaylist Item
        playlist = CreatePlaylist()
        # Fetch all Tracks from the playlist
        track_list = playlist.fetch_tracks_from_playlist(playlist_id)
        print(track_list)
        recommendations_list = []

        # Get all Recommendations from track IDs, limit to 50
        i=0
        for track in track_list:
            print(track)
            while i < 50:
                i += 1
                recommendations_list.append(track_recommendations(track)) 
        return recommendations_list

    
    #Get Track ID from session
    playlist_id = st.session_state.playlist_id

    #Build a Dataframe with Track Recommendations
    uris = playlist_recommendations(playlist_id)
    df_recommendations = pd.DataFrame(uris)
    
    #Building a Checkbox Column
    df_recommendations['select'] = True
    select = df_recommendations.pop('select')
    df_recommendations.insert(0, 'select', select)

    # Interface for track recommendations
    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = []
    
    col_title, col_logout = st.columns([6,1])
    
    with col_title:
        st.title('Sentify Music Recommender')
    
    with col_logout:
        st.title(" ")
        if st.button("Logout"):
            st.switch_page('pages/Login.py')

    st.data_editor(
        df_recommendations[:30],
        column_config={
            "select": st.column_config.CheckboxColumn(
                "Add to playlist?",
                help="Select your **favorite** recommendations",
                default=True,
            )
        },
    hide_index=True
    )

    col1, col2, col3, space = st.columns([1,1,1,1])

    with col1:
        if st.button('Settings'):
            pass

    with col2:
        if st.button('Shuffle'):
            pass

    with col3:
        if st.button('Go Back'):
            pass

    # Interface for playlist creation
    playlist_name = st.text_input('Enter the name of your new playlist:')

    if st.button('Create Spotify Playlist'):
        spotify_api = CreatePlaylist()
        my_playlist = spotify_api.create_playlist(name=playlist_name, description="My new playlist created by Sentify!")
        spotify_api.add_tracks_to_playlist(my_playlist['id'], uris)
        st.toast("Exporting Recommendations", icon='⌛')
        time.sleep(3)
        st.toast("Successfully exported Sentify Recommendations!", icon='🎉')


if __name__ == "__main__":
    run()