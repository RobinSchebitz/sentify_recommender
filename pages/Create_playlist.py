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
    st.title('Choose a Playlist')
    
    # Input field for songs
    #st.text_input("Enter Song Names", placeholder="Type song names here...")

    
    # Assuming playlists is a list of dictionaries where each dictionary has keys 'name' and 'id'
    playlists = [
        {"name": "Playlist 1", "id": "id1"},
        {"name": "Playlist 2", "id": "id2"},
        {"name": "Playlist 3", "id": "id3"}
    ]  # Replace this with your actual list of dictionaries

    # Create a radio button for each playlist
    selected_playlist_index = st.radio(username + "'s playlists", range(len(playlists)), format_func=lambda i: playlists[i]['name'])

    # Get the name of the selected playlist
    selected_playlist_name = playlists[selected_playlist_index]['name']

    # Display the selected playlist name
    st.write(f"You selected: {selected_playlist_name}")


    """# Button to navigate to the Settings page (Page 3)
    if st.button("Go to Preview"):
        st.switch_page('pages/Preview.py')
        
    # Button to generate the playlist
    if st.button("Generate Playlist"):
        st.write("Playlist would be generated here.")
        # Logic for generating the playlist would go here
        st.switch_page('pages/')"""
                  

if __name__ == "__main__":
    run()