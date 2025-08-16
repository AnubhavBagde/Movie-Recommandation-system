# app.py
import streamlit as st
import pickle as pkl
import pandas as pd

st.title("Movie Recommendation System")

# Load data
movies = pkl.load(open("list_of_movies.pkl", "rb"))
movies_list = movies["title"].values
cs = pkl.load(open("similarity.pkl", "rb"))

# Load offline posters
posters_df = pd.read_csv("movie_posters.csv")

def recommend(movie):
    """Return list of recommended movie names and posters."""
    find_index = movies[movies["title"] == movie].index[0]
    distances = cs[find_index]
    recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for idx, _ in recommended:
        title = movies.iloc[idx].title
        recommended_movies.append(title)
        # Fetch from saved poster DataFrame
        poster_url = posters_df.loc[posters_df["title"] == title, "poster_url"].values[0]
        recommended_posters.append(poster_url)

    return recommended_movies, recommended_posters

# UI
select = st.selectbox("Select a movie", movies_list)

if st.button("Recommend"):
    names, posters = recommend(select)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        col.image(poster, caption=name)

