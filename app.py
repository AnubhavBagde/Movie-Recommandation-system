import streamlit as st
import pickle as pkl
import pandas as pd
import requests
import os
import gdown

# Google Drive file IDs (replace with your actual ones)
MOVIES_FILE_ID = "15z2AluOGbfSZwPT31knyv7Lhs3QgKOi_"
SIMILARITY_FILE_ID = "1I0DqNa8c6O6eDLhxS22xta2pdnoI4I-r"

# Download helper
def download_file_from_gdrive(file_id, output):
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        st.sidebar.write(f"⬇️ Downloading {output} ...")
        gdown.download(url, output, quiet=False)

# Ensure required files exist
download_file_from_gdrive(MOVIES_FILE_ID, "list_of_movies.pkl")
download_file_from_gdrive(SIMILARITY_FILE_ID, "similarity.pkl")

# Load data
movies = pkl.load(open("list_of_movies.pkl", "rb"))
similarity = pkl.load(open("similarity.pkl", "rb"))

# Fetch poster (from pre-fetched CSV or API fallback)
posters_df = pd.read_csv("movie_posters.csv")

def fetch_poster(title):
    row = posters_df[posters_df["title"] == title]
    if not row.empty:
        return row.iloc[0]["poster_url"]
    return "https://via.placeholder.com/500x750?text=No+Poster"

# Recommendation function
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in distances:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_movies, recommended_posters

# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox("Choose a movie:", movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
