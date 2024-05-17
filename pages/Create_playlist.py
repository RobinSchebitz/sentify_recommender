import streamlit as st
from CreatePlaylist import CreatePlaylist

def run():
    username = st.session_state.user_name
    spotify_api = CreatePlaylist()
    playlists = spotify_api.fetch_playlists_user(username)
    
    st.title("Sentify Music Recommender")
    st.title(' ')
    st.title('Welcome ' + username)
    st.title(' ')
    
    
    # Input field for songs
    #st.text_input("Enter Song Names", placeholder="Type song names here...")

    col1, buff, col2 = st.columns([2,1,2])

    with col1:
        st.subheader('Choose a Playlist')
        # Assuming playlists is a list of dictionaries where each dictionary has keys 'name' and 'id'
        playlist_dict = {}
        for playlist in playlists['items']:
            playlist_dict[playlist['name']] = playlist['id']
        
        # Create a selectbox option for each playlist
        selected_playlist_index = st.selectbox(username + "'s playlists", list(playlist_dict.keys()))

        """ # Get the name of the selected playlist
        selected_playlist_name = playlists[selected_playlist_index]['name']

        # Display the selected playlist name
        st.write(f"You selected: {selected_playlist_name}") """

    with col2:
        st.subheader('Or choose a Song')
        user_input = st.text_input('Enter your favorite song:')   
        
        

    col3, buff, col4 = st.columns([2,1,2])
    
    with col3:
        if col3.button("Show Playlist"):
                st.switch_page('pages/Preview.py')

    with col4:
         if col4.button("Show Tracks"):
            st.switch_page('pages/Preview.py')
         

    
    
    # Button to navigate to the Settings page (Page 3)
    if st.button("Go to Preview"):
        st.switch_page('pages/Preview.py')
        
                  

if __name__ == "__main__":
    run()