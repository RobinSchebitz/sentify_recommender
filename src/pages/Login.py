import streamlit as st

if 'user_name' not in st.session_state:
    st.session_state['user_name'] = []
if 'playlist_id' not in st.session_state:
    st.session_state['playlist_id'] = ' '
if 'playlist_name' not in st.session_state:
    st.session_state['playlist_name'] = ' '
if 'track_id' not in st.session_state:
    st.session_state['track_id'] = ' '
if 'song' not in st.session_state:
    st.session_state['song'] = True
if 'recommendations' not in st.session_state:
    st.session_state['recommendations'] = []

def run():

    #Columns for Logo Alignment
    buffer, col1, buffer = st.columns([1,10,1])

    with col1:
        #Sentify Logo
        st.image('../images/sentify_fade.png')
        #Spotify Login
        st.title('Use your Spotify Account')
        user_name = st.text_input('Username')
        st.session_state.user_name = user_name
        st.text_input('Password', type='password')
        #Login Button
        if st.button('Login'):
            st.switch_page('pages/Create_playlist.py')

if __name__ == "__main__":
    run()