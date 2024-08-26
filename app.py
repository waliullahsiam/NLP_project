import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=7459ed6ce4fac7224d756a995754922c&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    
    if 'poster_path' in data and data['poster_path'] is not None:
        poster_path = data['poster_path']
        full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return None  # Handle cases where the poster is not found

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies_name = []
    recommended_movies_poster = []

    for i in distances[1:6]:  # Skip the first one since it's the same movie
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_name.append(movies.iloc[i[0]]['title'])
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies_name, recommended_movies_poster

st.header("Movies Recommendation System Using NLP")

with open('movies.pkl', 'rb') as file:
    movies = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

movie_list = movies['title'].values
selected_movie = st.selectbox('Type a name to see recommendations', movie_list)

if st.button('Show recommendations'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])  # Use st.image for displaying posters
        
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
        
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
        
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
        
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])
