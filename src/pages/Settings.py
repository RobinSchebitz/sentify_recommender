import streamlit as st

def run():
   
    buff, col_logo, buff = st.columns([1,10,1])
    
    with col_logo:

        st.image('../images/sentify_fade.png')

        on1 = st.toggle("Sentiment Switcher", help="Shows you recommendations from different sentiments instead")

        on2 = st.toggle("Good Vibes Only", help="Keep only recommendations from Happy & Uplifting Sentiment")

        options = st.multiselect("Sentiment Selection",
        ("Happy 😊", "Sad 😢", "Romantic 💖", "Energetic ⚡", "Calm 🧘", "Melancholic 🤔", "Uplifting 🌟"),
        help="Choose the sentiment you like")

        if st.button('Confirm'):
            if st.session_state.song:
                st.switch_page('pages/Song_Preview.py')
            else:
                st.switch_page('pages/Playlist_Preview.py')

if __name__ == "__main__":
    run()