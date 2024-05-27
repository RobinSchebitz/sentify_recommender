import streamlit as st
from pages import Create_playlist, Export, Song_Preview, Playlist_Preview, Login

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Page1'

# Page navigation
st.set_page_config(
    initial_sidebar_state='collapsed'
)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login","Create_playlist", "Song_Preview","Playlist_Preview", "Export"])

if page == "Login":
    Login.run()
elif page == "Create_playlist":
    Create_playlist.run()
elif page == "Song_Preview":
    Song_Preview.run()
elif page == "Playlist_Preview":
    Playlist_Preview.run()
elif page == "Export":
    Export.run()