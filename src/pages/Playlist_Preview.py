import streamlit as st
from CreatePlaylist import CreatePlaylist
import pandas as pd
import scipy as sp
import time

def run():
    # Import the necessary data & model
    df_spotify = pd.read_pickle('../data/sentify.pkl')

    sim_matrix = sp.sparse.load_npz('../models/sentify.npz')

    sim_matrix_df = pd.DataFrame.sparse.from_spmatrix(sim_matrix)

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
        recommendations_list = []
        recommendations_df = pd.DataFrame()

        # Get all Recommendations from track IDs, limit to 50
        for track in track_list:
            recommendations_list.append(track_recommendations(track).to_frame(name='track_uri'))
        
        if recommendations_list:
            recommendations_df = pd.concat(recommendations_list, ignore_index=False)

        return recommendations_df

    #Put Song Boolean False
    st.session_state.song = False

    #Get Track ID from session
    playlist_id = st.session_state.playlist_id

    #Build a Dataframe with Track Recommendations
    uris = playlist_recommendations(playlist_id)
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
    df_recommendations[' 🎧'] = '   ▶'
    
    buffer, col_logo, buffer = st.columns([1,10,1])

    with col_logo:
        st.image('../images/sentify_fade.png')
    
        col_title, buffer = st.columns([6,1])
        
        with col_title:
            st.write("Your selected Playlist:")
            st.write("*"+ st.session_state.playlist_name +"*")
            st.write("Recommendations:")
        
        st.data_editor(
            df_recommendations[:30],
            column_config={
                "select": st.column_config.CheckboxColumn(
                    "Add to playlist?",
                    help="Select your **favorite** recommendations",
                    default=True,
                ), "Song": st.column_config.Column(width="medium"), "track_uri": None
            },
        hide_index=True, disabled=True
        )

        col1, col2, col3 = st.columns([2,2,2])

        with col1:
            if st.button('Settings'):
                st.switch_page('pages/Settings.py')

        with col2:
            if st.button('Shuffle'):
                pass
        
        with col3:
            if st.button('Go Back'):
                st.switch_page('pages/Create_playlist.py')
        
        st.title(" ")
        
        col_4, buffer = st.columns([5,1])

        with col_4:

            # Interface for playlist creation
            playlist_name = st.text_input('Enter the name of your new playlist:')

        col_bot1, col_bot2, buffer = st.columns([3,3,1])

        with col_bot1:

            if st.button('Create Spotify Playlist'):
                spotify_api = CreatePlaylist()
                my_playlist = spotify_api.create_playlist(name=playlist_name, description="My new playlist created by Sentify!")
                uris = uris.squeeze()
                spotify_api.add_tracks_to_playlist(my_playlist['id'], uris)
                st.toast("Exporting Recommendations", icon='⌛')
                time.sleep(3)
                st.toast("Successfully exported Sentify Recommendations!", icon='🎉')
                time.sleep(3)
                st.switch_page('pages/Create_playlist.py')
        
        with col_bot2:

            if st.button('Add to ' + st.session_state.playlist_name):
                spotify_api = CreatePlaylist()
                uris = uris.squeeze()
                spotify_api.add_tracks_to_playlist(playlist_id, uris)
                st.toast("Exporting Recommendations", icon='⌛')
                time.sleep(3)
                st.toast("Successfully exported Sentify Recommendations!", icon='🎉')
                time.sleep(3)
                st.switch_page('pages/Create_playlist.py')


if __name__ == "__main__":
    run()