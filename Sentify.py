import streamlit as st
from pages import Create_playlist, Export, Preview, Login

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Page1'

# Page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login","Create_playlist", "Preview", "Export"])

if page == "Login":
    Login.run()
elif page == "Create_playlist":
    Create_playlist.run()
elif page == "Preview":
    Preview.run()
elif page == "Export":
    Export.run()

#st.page_link("pages/Home.py", label="Home", icon="🏠")
#st.page_link("pages/About.py", label="About", icon="1️⃣")
#st.page_link("pages/Contact.py", label="Contact", icon="🌎")