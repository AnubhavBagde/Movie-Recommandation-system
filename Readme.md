# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built with Python, Machine Learning, and Streamlit. The app suggests movies similar to the one selected by the user and displays their posters using pre-fetched data from TMDB.

📌 Features

Select any movie from a dropdown list.

Get top 5 recommended movies based on similarity scores.

View movie posters for recommended films.

Runs on Streamlit with a clean and interactive UI.

Offline-friendly → posters are stored in a CSV (movie_posters.csv) so the app doesn’t rely on API calls.

# 🛠️ Tech Stack

Python

Pandas – Data handling

Pickle – For saving/loading preprocessed data and similarity matrix

Scikit-learn – Cosine similarity (vectorization)

Streamlit – Web app interface

TMDB API – For fetching movie posters (saved offline for stability)
git clone https://github.com/AnubhavBagde/Movie-Recommandation-system
cd movie-recommendation-system


pip install -r requirements.txt

# Future Improvements

Hybrid recommendation (content + collaborative filtering).

Integration with live TMDB API calls.

Improved UI/UX with more movie details (rating, overview, release year).

# 🙌 Acknowledgements

The Movie Database (TMDB) for posters and metadata.

Streamlit for the web framework.

