import streamlit as st
import pickle
import requests
import gdown


from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
api_key = os.getenv("API_KEY")


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    # Get the index of the movie in the dataset based on its title
    movie_index = movies[movies['title'] == movie].index[0]

    # Sort the movies based on similarity score in descending order and get top 10, excluding the first movie itself
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movies_posters = []

    # Print the titles of the top 10 most similar movies
    for i in distances[1:11]:
        # Access movie_id directly from the 'movie_id' column
        movie_id = movies.iloc[i[0]].movie_ID
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movies_posters


st.header('Movie Recommender System')

# Load data
movies = pickle.load(open('./movies.pkl', 'rb'))

# Direct Google Drive shareable link
url_drive = 'https://drive.google.com/uc?id=1Tl63LJZ2MPmilnFyQHD0I9Q72heUXIhz'
output = 'similarity.pkl'

# Download the file
if not os.path.exists('similarity.pkl'):
    gdown.download(url_drive, 'similarity.pkl', quiet=False)

# Now, load the file after it's been downloaded
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values

# Streamlit UI
selected_movie = st.selectbox(
    'Type or select a movie from the dropdown',
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Define fixed height for titles
    title_height = "70px"

    # First row (Movies 1 to 5)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(
                f"<div style='height: {title_height}; display: flex; align-items: center; justify-content: center; text-align: center; font-size: 14px; font-weight: bold;'>{recommended_movie_names[i]}</div>",
                unsafe_allow_html=True
            )
            st.image(recommended_movie_posters[i], use_container_width=True)

    # Add spacing between rows
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Second row (Movies 6 to 10)
    cols = st.columns(5)
    for i in range(5, 10):
        with cols[i - 5]:  # Reset index for second row
            st.markdown(
                f"<div style='height: {title_height}; display: flex; align-items: center; justify-content: center; text-align: center; font-size: 14px; font-weight: bold;'>{recommended_movie_names[i]}</div>",
                unsafe_allow_html=True
            )
            st.image(recommended_movie_posters[i], use_container_width=True)
