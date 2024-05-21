import streamlit as st

if 'user_name' not in st.session_state:
    st.session_state.user_name = []

def run():
    st.title('Sentify Music Recommender')
    st.title(' ')
    st.title(' ')
    st.title(' ')
    st.title('Use your Spotify Account')

    
    user_name = st.text_input('Username')
    st.session_state.user_name = user_name 
    st.text_input('Password', type='password')

    if st.button('Login'):
        st.switch_page('pages/Create_Playlist.py')

if __name__ == "__main__":
    run()