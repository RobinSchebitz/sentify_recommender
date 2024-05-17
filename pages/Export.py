import streamlit as st

def run():
    st.title("Generated Playlist")

    # Placeholder for generated playlist
    st.write("This is where the generated playlist would be shown.")
    
    # Button to export playlist to Spotify
    if st.button("Export to Spotify"):
        st.write("Export functionality would be implemented here")

    # Button to go back to the song input page
    if st.button("Back to Song Input"):
        st.switch_page('pages/Create_playlist.py')

    #st.page_link("pages/Home.py", icon="🏠")
    #st.page_link("pages/About.py", icon="1️⃣")
    #st.page_link("pages/Contact.py", icon="🌎")

if __name__ == "__main__":
    run()