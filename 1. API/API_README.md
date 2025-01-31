# Movie Data Collection and Analysis

This project involves collecting, cleaning, and enriching movie data from the Movie Database (TMDb) API and then performing analysis on the final dataset. The dataset consists of movie details, including general information, budget, revenue, genres, production companies, runtime, cast, crew, and keywords. The project demonstrates how to handle APIs, process and clean data, and merge datasets.

## Project Overview

- **Data Collection**: Movie data is fetched from the TMDb API.
- **Data Cleaning**: Raw data is cleaned to remove duplicates and line breaks.
- **Enrichment**: Additional details like cast, crew, and keywords are fetched for each movie.
- **Dataset Merging**: Multiple datasets are merged to create a final enriched dataset containing all the required information for each movie.

## Key Features

- Fetches movie data from the TMDb API using Python.
- Cleans data by removing duplicates and handling missing values.
- Enriches data by adding cast, crew, and keyword information.
- Saves cleaned and enriched data to CSV files for analysis.

## Dependencies

- `requests`: For making API requests.
- `pandas`: For data manipulation and analysis.
- `time`: For controlling the request rate to the TMDb API.
- `warnings`: For ignoring future warnings during API calls.

You can install the necessary dependencies using pip:

```bash
pip install requests pandas
```

## Setting Up Your TMDb API Key

To fetch movie data, you'll need to have a valid **TMDb API key**. Follow these steps to obtain one:

1. Go to the [TMDb API website](https://www.themoviedb.org/documentation/api).
2. If you don't already have an account, click on **Sign Up** to create one.
3. Once you're logged in, navigate to your account settings by clicking on your profile picture in the top-right corner and selecting **Account Settings**.
4. In the left sidebar, select **API** under the **Access** section.
5. On the API page, click the **Create** button to generate a new API key.
6. Copy the API key once it's generated.

Once you have the API key, you need to add it to the project.

## Steps
### **1. Fetching Movie Data**

The movie data is fetched from the TMDb API using the /movie/popular endpoint, which retrieves a list of popular movies. The data is collected across multiple pages and stored in a data frame.

```python
response = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={j}').json()
```

The data includes:

- Title
- Overview
- Original Language
- Release Date
- Popularity
- Vote Count
- Vote Average
The movie data is saved in a CSV file called Movies.csv.

### **2. Data Cleaning**

The dataset is cleaned by replacing line breaks in the overview column to ensure the data is readable and consistent. Duplicates based on `movie_ID` are also removed.
```python
df['overview'] = df['overview'].replace({r'\n': ' ', r'\r': ' '}, regex=True)
df.to_csv('Cleaned_Movies.csv', index=False)
```
`Cleaned_Movies.csv` (an intermediate file) is not uploaded to the repository as it is only used for cleaning purposes and has no further use in the analysis or recommender system.

### **3. Fetching Movie Details**

Additional details such as budget, genres, production companies, revenue, and runtime are fetched for each movie using the `movie ID`.
```python
response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}').json()
```
These details are stored in a new CSV file called `Details.csv` (not uploaded to GitHub as it is another intermediate file with no further use).


### **4. Merging Datasets**

The movie details are merged with the cleaned movie dataset based on the ``movie_ID`` column. The merged dataset is saved as `Combined_Movies_Details.csv`.
```python
combined_df = pd.merge(cleaned_movies_df, updated_details_df, on='movie_ID', how='left')
combined_df.to_csv('../data/Combined_Movies_Details.csv', index=False)
```

### **5. Adding Cast and Crew Details**

The cast and crew details, including the director and top 3 actors, are fetched for each movie using the `/movie/{movie_id}/credits` API endpoint.
```python
response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}').json()
```
These details are saved in `Movie_Crew_Details.csv`.

### **6. Adding Keywords**

Movie keywords are fetched using the `/movie/{movie_id}/keywords` API endpoint and stored in `movie_keywords.csv`.
```python
response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key={api_key}&language=en-US').json()
```

### **7. Final Merging**

The final dataset is created by merging the combined dataset with the movie keywords. The final dataset is saved as `complete_movie_dataset.csv`.\

```python
updated_movie_dataset = complete_movie_dataset.merge(movie_keywords, on='movie_ID', how='left')
updated_movie_dataset.to_csv('../data/complete_movie_dataset.csv', index=False)
```
### **8. Final Dataset**

The final dataset contains the following columns:
- movie_ID
- title
- overview
- original_language
- release_date
- popularity
- vote_count
- vote_average
- budget
- genres
- homepage
- production_companies
- production_countries
- revenue
- runtime
- director
- top_actors
- keywords

### **9. Data Analysis** 
(Future Steps - in `2. Exploratory Data Analysis Folder`)

Once the dataset is prepared, it can be used for further analysis, such as:

- Genre distribution analysis.
- Fetching top 10 genres, actors, directors, revenue etc
- Analysing average runtime, average voting
- Release year distribution
- Top genre combinations
- Correlation between columns

```bash
/data
    Combined_Movies_Details.csv
    complete_movie_dataset.csv
    Movie_Crew_Details.csv
/movie_keywords.csv
README.md

```
**Note**

Note: The following intermediate files are not included in the repository because they are used only during the data processing and cleaning stages:

`Movies.csv`: Raw movie data from the API.
`Cleaned_Movies.csv`: Cleaned version of the movie data.
`Details.csv`: Detailed movie information fetched from the API.

These files are generated during the execution of the notebook and are not necessary for further analysis or the recommendation system.


## Notes

Make sure to replace 'api_key_here' with your actual TMDb API key in the code.
The API rate limit is respected by adding delays between API requests to avoid overloading the server.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.











































