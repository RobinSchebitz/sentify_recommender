import streamlit as st

def run():

    option = st.selectbox(
        "Current Mood Selection",
        ("Happy", "Sad", "Romantic", "Energetic", "Calm", "Melancholic", "Uplifting"))

    st.write("You selected:", option)

    on = st.toggle("Mood Switcher")

    on = st.toggle("Genre Selection")

    #Importing track id from previous session
    track_id = st.session_state.track_id
    
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    
    with col4:
        if st.button('Confirm'):
            st.session_state.track_id = track_id
            st.switch_page('pages/Song_Preview.py')


if __name__ == "__main__":
    run()