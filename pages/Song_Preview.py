import streamlit as st
from CreatePlaylist import CreatePlaylist
import pandas as pd
import numpy as np
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

    
    if 'track_id' not in st.session_state:
        st.session_state.playlist_id = " "

    #Get Track ID from session
    track_id = st.session_state.track_id

    #Build a Dataframe with Track Recommendations
    uris = track_recommendations(track_id)
    df_recommendations = pd.DataFrame(uris)

    #Add Artist and Track Information
    df_merged = df_recommendations.merge(df_spotify[['artist_name', 'track_name']], how='left', left_index=True, right_index=True)
    df_merged = df_merged.rename(columns={'artist_name': 'Artist', 'track_name': 'Song'})
    df_recommendations = df_merged

    #Building a Checkbox Column
    df_recommendations['select'] = True
    select = df_recommendations.pop('select')
    df_recommendations.insert(0, 'select', select)

    #Building a Play Button Column
    df_recommendations['play'] = '▶'

    # Interface for track recommendations
    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = df_recommendations
    
    buffer, col_logo, buffer = st.columns([1,5,1])

    with col_logo:
        st.image('images/sentify_fade.png')

    col_title, buffer = st.columns([6,1])
    
    with col_title:
        desired_row = df_spotify[df_spotify['track_uri'] == track_id]

        if not desired_row.empty:
            # Check if there's a matching row
            artist_name = desired_row['artist_name'].values[0]
            track_name = desired_row['track_name'].values[0]
        else:
            # Handle the case where no row matches the track_id
            artist_name = None
            track_name = None

        st.title("Your favorite Song:")

        table_html = f"""
        <table style="border: none;">
        <tr>
            <th>Artist</th>
            <th>Song</th>
        </tr>
        <tr>
            <td>{artist_name}</td>
            <td>{track_name}</td>
        </tr>
        </table>
        """

        st.write(table_html, unsafe_allow_html=True)
        st.title("Sentify Recommendations:")
    
    st.data_editor(
        df_recommendations,
        column_config={
            "select": st.column_config.CheckboxColumn(
                "Add to playlist?",
                help="Select your **favorite** recommendations",
                default=True,
            ), "track_uri": None
        },
    hide_index=True
    )

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        if st.button('Settings'):
            st.switch_page('pages/Settings.py')

    with col2:
        if st.button('Shuffle'):         
            st.session_state.recommendations = st.session_state.recommendations.sample(frac=1).reset_index(drop=True)                        

    with col3:
        if st.button('Go Back'):
            st.switch_page('pages/Create_Playlist.py')

    
    col_bot, buffer = st.columns([3,2])

    with col_bot:

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