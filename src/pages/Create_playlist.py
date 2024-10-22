import streamlit as st
from CreatePlaylist import CreatePlaylist

def run():
    
    username = st.session_state.user_name
    spotify_api = CreatePlaylist()
    playlists = spotify_api.fetch_playlists_user(username)

    buffer, col_logo, buffer = st.columns([1,10,1])

    with col_logo:
        st.image('../images/sentify_fade.png')

        col_title, col_logout = st.columns([6,1])

        with col_title:
            st.title('Welcome ' + username + '!')

        with col_logout:
            st.title(" ")
            if st.button("Logout"):
                st.switch_page('pages/Login.py')

        col1, buff, col2 = st.columns([3,1,3])

        with col1:
            st.subheader('Choose a Playlist')
            # Assuming playlists is a list of dictionaries where each dictionary has keys 'name' and 'id'
            playlist_dict = {}
            for playlist in playlists['items']:
                playlist_dict[playlist['name']] = playlist['id']
            
            # Create a selectbox option for each playlist
            selected_playlist = st.selectbox(username + "'s playlists", list(playlist_dict.keys()))

            if col1.button("Playlist Recommendation"):
                playlist_id = playlist_dict[selected_playlist]
                st.session_state.playlist_name = selected_playlist
                st.session_state.playlist_id = playlist_id
                st.switch_page('pages/Playlist_Preview.py')

        with col2:
            st.subheader('Or choose a Song')
            track_id = st.text_input('Enter your favorite Song ID:', value='spotify:track:')

            if col2.button("Tracks Recommendation"):
                st.session_state.track_id = track_id
                st.switch_page('pages/Song_Preview.py')  
                  
if __name__ == "__main__":
    run()