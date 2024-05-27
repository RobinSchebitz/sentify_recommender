# About
Here you find our jupyter notebook files for running a content based music recommender model based on an modified version of the 1 Million playlists data set provided by Spotify.

The data used is a modified version of the [challenge dataset from the Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#challenge-dataset).

# Getting this project to run
There are two ways to do it: 

## Quickstart with pre-selected model features:
1. Clone the repository.
2. Install the required packages using ```pip install -r requirements.txt```.
3. Download the [challenge dataset from the Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#challenge-dataset) and store in in the data folder.
4. Send us a request to obtain the final dataset and the related cosine similarity matrix to run the streamlit app.
5. Create a .env file with your Spotify credentials obtained from [Spotify](https://developer.spotify.com). Assign your credentials to the following keys:
    - spotify_client_id=*Your Spotify client id here*
    - spotify_client_secret=*Your Spotify client secret here*
6. Place the files you received in their respective folders.
    - The .npz file goes into the model folder and the .csv file goes into the data folder.
7. Run the sentify_model_quickstart.ipynb file.
8. Run ```streamlit run Sentify.py```.

## Quickstart with custom model features:
1. Clone the repository.
2. Install the required packages using ```pip install -r requirements.txt```.
3. Download the [challenge dataset from the Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#challenge-dataset) and store in in the data folder.
4. Send us a request to obtain the final dataset to compute your own cosine similarity matrix and run the streamlit app.
5. Create a .env file with your Spotify credentials obtained from [Spotify](https://developer.spotify.com). Assign your credentials to the following keys:
    - spotify_client_id=*Your Spotify client id here*
    - spotify_client_secret=*Your Spotify client secret here*
6. Place the .csv file in the data folder.
7. Open sentify_model.ipynb and modify the selection of features then run the file.
8. Run ```streamlit run Sentify.py```

## Run project from scratch:
*Please beware: You might run into multiple undocumented issues here including API timeouts!*
1. Clone the repository.
2. Install the required packages using ```pip install -r requirements.txt```.
3. Download the [challenge dataset from the Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#challenge-dataset) and store in in the data folder.
4. Create a .env file with your Spotify credentials obtained from [Spotify](https://developer.spotify.com) and [Genius]()Assign your credentials to the following keys:
    - spotify_client_id=*Your Spotify client id here*
    - spotify_client_secret=*Your Spotify client secret here*
    - genius_client_id=*Your Genius client id here*
    - genius_client_secret=*Your Genius client secret here*
    - genius_token=*Your Genius token here*
4. Run *notebookname* notebook to update the original challenge data and obtain cleaned_data.csv
    - The .csv file goes into the data folder.
5. Run *notebookname* notebook to obtain the lyrics.csv that contains all available lyrics data. 
    - The .csv file goes into the data folder.
6. Run *notebookname* notebook to obtain the genre.csv file containing a dummy encoded dataframe.
    - The .csv file goes into the data folder.
7. Run the sentify_model.ipynb file 
7. Place the files you received in their respective folders.
    - The .npz file goes into the model folder and the .csv file goes into the data folder.
8. Run ```streamlit run Sentify.py```


## Requirements:
- pyenv with Python: 3.11.3

## Setup

Use the requirements file in this repo to create a new environment.

```pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements_dev.txt
```
