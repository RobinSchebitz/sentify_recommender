import streamlit as st

def run():
    st.title('Preview')

    # Settings fields
    st.write("Settings can be previewed here.")
    st.slider("Setting 1", min_value=0, max_value=100, value=50)
    st.selectbox("Setting 2", ["Option 1", "Option 2", "Option 3"])

    # Button to confirm settings and go back to Page 2
    if st.button("Confirm Settings"):
        st.switch_page('pages/Create_playlist.py')

    #st.page_link("pages/Home.py", icon="🏠")
    #st.page_link("pages/About.py", icon="1️⃣")
    #st.page_link("pages/Contact.py", icon="🌎")

if __name__ == "__main__":
    run()