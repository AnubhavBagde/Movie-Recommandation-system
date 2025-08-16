# save_posters.py
import pickle as pkl
import requests
import pandas as pd
from tqdm import tqdm

API_KEY = "046a3998164ea67649fcf593f2d5955c"

# Load your movies dataset
movies = pkl.load(open("list_of_movies.pkl", "rb"))

def fetch_poster_url(title):
    """Search TMDB for a movie by title and return the poster URL."""
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
        response = requests.get(search_url, timeout=5).json()
        if response.get("results"):
            poster_path = response["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

# Create a DataFrame for title → poster_url
poster_data = []
for title in tqdm(movies["title"].values):
    poster_data.append({
        "title": title,
        "poster_url": fetch_poster_url(title)
    })

posters_df = pd.DataFrame(poster_data)

# Save poster URLs for offline use
posters_df.to_csv("movie_posters.csv", index=False)
print("Poster URLs saved to movie_posters.csv")
