import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=aa6defe3e5ed395696b17cf7286591b8".format(movie_id)
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
            full_path = TMDB_IMAGE_BASE_URL + poster_path
            return full_path
        else:
            print("Poster path not found for movie ID:", movie_id)
            return None
    else:
        print("Error fetching movie data:", data.status_code)
        return None

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")

# Create a dropdown to select a movie
selected_movie = st.selectbox("Select a movie:", movies_list)


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        poster_url = fetch_poster(movies_id)
        if poster_url:
            recommend_poster.append(poster_url)
        else:
            recommend_poster.append("NA")  # Handle missing posters (optional)
    return recommend_movie, recommend_poster

if st.button("Recommend"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        if movie_poster[0] != "NA":
            st.image(movie_poster[0])
        else:
            st.write("Poster unavailable")  # Handle missing posters (optional)
    with col2:
        st.text(movie_name[1])  # Adjust index for each column
        if movie_poster[1] != "NA":
            st.image(movie_poster[1])
        else:
            st.write("Poster unavailable")  # Handle missing posters (optional)
    with col3:
        st.text(movie_name[2])  # Adjust index for each column
        if movie_poster[2] != "NA":
            st.image(movie_poster[2])
        else:
            st.write("Poster unavailable")  # Handle missing posters (optional)
    with col4:
        st.text(movie_name[3])  # Adjust index for each column
        if movie_poster[3] != "NA":
            st.image(movie_poster[3])
        else:
            st.write("Poster unavailable")  # Handle missing posters (optional)
    with col5:
        st.text(movie_name[4])  # Adjust index for each column
        if movie_poster[4] != "NA":
            st.image(movie_poster[4])
        else:
            st.write("Poster unavailable")  # Handle missing posters (optional)