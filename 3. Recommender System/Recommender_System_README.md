# Recommender System

## Overview

A recommender system is a machine learning model designed to suggest items, products, or content to users based on various criteria. This project implements a content-based movie recommender system that suggests movies based on their features, including overview, genres, director, actors, and keywords.

### Dataset

The dataset used in this project is complete_movie_dataset.csv, which contains 9,130 movies with the following key attributes:

- `movie_ID`: Unique identifier for each movie
- `title`: Movie title
- `overview`: Brief movie description
- `genres`: Genre classification of the movie
- `director`: Name of the movie's director
- `top_actors`: Leading actors in the movie
- `keywords`: Descriptive keywords associated with the movie

## Data Preprocessing

### Steps performed:

**1. Handling Missing Values**:

- Missing values in overview, director, top_actors, and keywords were replaced with an empty string.
- Verified that no null values remained after processing.

**2. Removing Duplicates**:

- Checked and confirmed that there were no duplicate entries in the dataset.

**3. Converting String Data to Lists**:

- genres, top_actors, and keywords were converted from string format to Python lists.

**4. Text Processing**:

- Spaces within genres, overview, director, and top_actors were removed to standardize text formatting.

**5. Feature Engineering**:

Created a new column `tags`, which is a concatenation of overview, genres, director, top_actors, and keywords. This will be used for similarity calculations.

### Stemming in Movie Recommendation System

- To improve text processing, we apply stemming to reduce words to their root form. This helps in better matching of movie-related terms.

- We use `PorterStemmer` from nltk to stem keywords before vectorization.

For example:  
- *"Loved"*, *"Loving"*, and *"Love"* → **"love"**  
- *"Watching"*, *"Watches"*, and *"Watched"* → **"watch"**  

### **Implementation**  
We use **NLTK’s PorterStemmer** to apply stemming.  

```python
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def stem_text(text):
    words = text.lower().split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)















