# Movie Recommendation System

## Overview
This project is a **content-based movie recommendation system** that suggests movies based on user input. It fetches movie details from the **TMDB API**, processes data, applies **TF-IDF vectorization**, and generates recommendations. The system is deployed on **Streamlit** for easy accessibility.

## Features
- **API Integration**: Fetches movie details(includes overview, keywords, top actors, director etc) from **TMDB**.
- **Data Processing**: Cleans and structures data efficiently.
- **EDA (Exploratory Data Analysis)**: Insights into movie data.
- **Content-Based Filtering**: Utilizes **TF-IDF** for movie similarity.
- **Evaluation**: Compared results with JioCinema’s top 10 recommendations.
- **Deployment**: Hosted on **Streamlit** with a user-friendly UI.

## Folder Structure
```
├── 1. API/                            # Scripts for fetching movie data from TMDB API
├── 2. Exploratory Data Analysis/      # Exploratory Data Analysis notebooks
├── 3. Recommender System/             # Model implementation and recommendation system
├── recommender-system/                # Streamlit app deployment files
├── data/                              # Processed datasets
├── README.md                          # Project overview (this file)
```

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/Sravya-T01/movie-recommendation.git
cd movie-recommendation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
## **3. Set Up API Key**
To ensure the **TMDB API Key** works across all components, use the following steps:

- **Option 1: Using a `.env` file**  
Create a `.env` file in the root directory and add your TMDB API Key. For security reasons, Git ignores this file (it’s included in `.gitignore`).
```bash
TMDB_API_KEY=your_api_key_here
```
- **Option 2: Using Streamlit Secrets**
For Streamlit deployment and added security, add the API key to the Streamlit Secrets. Create a secrets.toml file inside the .streamlit folder and add
```bash
TMDB_API_KEY=your_api_key_here
```
The API key will be accessed from both the .env file (in the code) and Streamlit Secrets (in the deployed app) to ensure seamless integration in both development and deployment environments.



### 4. Run the Streamlit App
```bash
streamlit run app.py
```

## Methodology
1. **API Data Collection**: Gathered movie details using TMDB API.
2. **Data Preprocessing**: Filtered relevant movie features, and extracted the top 3 actors.
3. **EDA**: Analyzed movie trends, genre distributions, and missing values.
4. **Feature Engineering**: Applied **TF-IDF** on movie descriptions and keywords.
5. **Recommendation Engine**: Used cosine similarity to suggest similar movies.
6. **Evaluation**: Compared recommendations with JioCinema using **precision@10**.
7. **Deployment**: Built a **Streamlit** UI for easy interaction.

## Future Improvements
- Adding collaborative filtering for personalized recommendations.
- Enhancing UI with search history and trending movies.
- Deploying as a web app with authentication features.

## **Sources**

- **TMDB API** for movie data.
- **Streamlit** for UI deployment.
- **JioCinema** for benchmarking recommendations.

