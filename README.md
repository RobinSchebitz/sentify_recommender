# About
Here you find our jupyter notebook files for running a content based music recommender model based on an modified version of the 1 Million playlists data set provided by Spotify.

The data used is a modified version of the [challenge dataset from the Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#challenge-dataset).

## Setup

Run this code to create a new environment. ```requirements.txt``` will install the necessary packages.

```
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


# Getting this project to run
There are two ways to do it: 

## Quickstart with pre-selected model features:
1. Clone the repository.
2. Install the required packages using ```pip install -r requirements.txt```.
3. Download the [challenge dataset from the Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge) from the ressources section. Then unzip it and store ```challenge_set.json``` in the data folder.
4. Create a .env file with your Spotify credentials obtained from [Spotify](https://developer.spotify.com). Assign your credentials to the following keys:
    - spotify_client_id=*Your Spotify client id here*
    - spotify_client_secret=*Your Spotify client secret here*
6. Place the received ```sentify_data.zip``` file into the ```data``` folder.
7. Run the ```sentify_model_quickstart.ipynb``` notebook.
8. If you now want to run the application please navigate to the source folder ```cd src```.
9. Run ```streamlit run Sentify.py```.

## Run project from scratch:
1-3. Follow steps from above.
4. Send us a request to obtain the data from google drive.
5. Create a .env file with your Spotify credentials obtained from [Spotify](https://developer.spotify.com) and [Genius]()Assign your credentials to the following keys:
    - spotify_client_id=*Your Spotify client id here*
    - spotify_client_secret=*Your Spotify client secret here*
6. Put the obtained data ```lyrics.zip``` and ```dummy_encoded_genres.zip``` in the ```data``` folder.
7. Run ```sentify_model.ipynb``` notebook.
8. If you now want to run the application please navigate to the source folder ```cd src```.
9. Run ```streamlit run Sentify.py```.

## Additional notes:
* In the notebook section **Drop unwanted features** you are able to decide which features you want to include for the recommender model. Be aware that some feature combinations may make the cosine similarity matrix too sparse. This may result in the fact that no similarity scores are computed.
* The login function on Sentify is only a mock-up, therefore you only need to put in your spotify username. The username is necessary to fetch playlist information and interact with your account.
* The settings window, including the buttons, the mood labels as well as the shuffle function are mock-ups and part of future work.
* There is an unsolved bug in which certain track_uri can not be found from the ```track_recommendations()``` function and Sentify will crash accordingly.
* If you want to see the results for a negative sentiment playlist of rock songs as in our presentation,  you can make a Spotify playlist with the following tracks: *spotify:track:59NqKTBxIYLZOqtgWna0J0* and *spotify:track3BVZmnvtniy5fGQdKaQrhD*.
