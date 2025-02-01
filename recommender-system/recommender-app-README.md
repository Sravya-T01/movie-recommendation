# Movie Recommender System - app

## Overview

This is a content-based movie recommender system built using Streamlit. The system recommends movies to users based on their similarity to the selected movie. It uses movie features such as title, overview, genres, director, top actors, and keywords to compute similarity scores and provide relevant movie suggestions.

### Technologies Used
- Streamlit: For the web-based UI to display recommendations.
- Pickle: For saving and loading movie data and similarity matrix.
- The Movie Database (TMDb) API: For fetching movie posters.
- Google Drive (gdown): For downloading the similarity matrix.

### Setup Instructions

#### Prerequisites

**1. Install required Python libraries**:
```bash
pip install streamlit requests gdown python-dotenv
```

**2. Create a `.env` file in the root directory and add your TMDb API key**:
```ini
API_KEY=your_tmdb_api_key
```

***Important*** 

Since the `.env` file is included in `.gitignore` to keep the API key secure, you must add your **TMDb API key** directly to **Streamlit Secrets** if deploying the app.
- When deploying to Streamlit Cloud, navigate to the app's dashboard and go to Settings → Secrets.
- Add your API_KEY as a secret:
```txt
API_KEY: your_tmdb_api_key
```

**3. Download the movies.pkl and similarity.pkl files**:

- movies.pkl: Contains the movie dataset.
- similarity.pk: Contains the precomputed movie similarity matrix.

**Note** 

The similarity.pkl file was stored on Google Drive and is larger than 100 MB, so it is not included in the GitHub repository. The file will be downloaded automatically when you run the app for the first time.
- Direct Google Drive link used for downloading: [https://drive.google.com/uc?id=1Tl63LJZ2MPmilnFyQHD0I9Q72heUXIhz](url)

**Optional**: If similarity.pkl is not already downloaded, it will be fetched from Google Drive automatically when the app is run.

## Running the Application

**1. To run the Streamlit app, execute the following command:**
``` bash
streamlit run recommender-system.py
```

Once the app is running, open your browser and go to [http://localhost:8501](url) to use the movie recommender system or when you run the code it will automatically open or give you a link

## How It Works

**1. Movie Data**: The movies.pkl file contains information about the movies, including their title, overview, genres, director, top actors, and keywords. This data is loaded into the app at runtime.

**2. Similarity Matrix**: The similarity.pkl file contains a precomputed cosine similarity matrix between movie vectors. If this file is not found locally, it will be downloaded from Google Drive using gdown.

**3. Movie Recommendation**:

- The user can select a movie from a dropdown list.
- Once the user clicks "Show Recommendation", the system computes the top 10 most similar movies based on the similarity matrix.
- The movie posters are fetched from the TMDb API using the movie IDs and displayed along with the movie titles.

**4. Display**:

- The top 10 recommended movies are displayed in two rows, each with five movie posters and titles.

## Code Explanation

* fetch_poster(movie_id): This function takes a movie ID, makes an API request to TMDb, and returns the full URL of the movie poster.

* recommend(movie): This function takes the movie title as input, finds the movie's index in the dataset, and sorts the movies based on their similarity scores. It then fetches the names and posters of the top 10 recommended movies.

* **Streamlit UI**:
  - The select box widget allows users to choose a movie from the dataset.
  - The Show Recommendation button triggers the recommendation generation.
  - The top 10 recommended movies are displayed in a 2x5 grid layout, each with a poster and title.

## Example

When you launch the app and select a movie like "Harry Potter and the Goblet of Fire", the system will recommend the top 10 most similar movies, displaying their posters and titles. The recommendations are based on content similarity calculated using the movie data.









