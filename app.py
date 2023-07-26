# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# def fetch_poster(movie_id):
#     response = requests.get(
#         'https://api.themoviedb.org/3/movie/{}?api_key=e326010ea6687efa202a6578c5092330&language=en-US'.format(
#             movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500" + data['poster_path']
#
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         # Assuming 'movie_id' is a column in the 'movies' DataFrame
#         movie_id = movies.iloc[i[0]]['movie_id']
#
#         recommended_movies.append(movies.iloc[i[0]]['title'])
#         # fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters
#
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     movies['title'].values)
#
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])

import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit.components.v1 import components


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=e326010ea6687efa202a6578c5092330&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        # Assuming 'movie_id' is a column in the 'movies' DataFrame
        movie_id = movies.iloc[i[0]]['movie_id']

        recommended_movies.append(movies.iloc[i[0]]['title'])
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load the movie_dict.pkl which contains 'movie_id', 'title', and other movie information
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

# Create the movies DataFrame from the dictionary
movies = pd.DataFrame(movies_dict)

# Assuming 'movie_id' is a column in the 'movies_dict', if not, modify the above code accordingly

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values)

def main():

    imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

    imageUrls = [
        fetch_poster(299536),
        fetch_poster(233),
        fetch_poster(101),
        fetch_poster(2830),
        fetch_poster(17455),
        fetch_poster(429422),
        fetch_poster(13972),
        fetch_poster(2),
        fetch_poster(22),
        fetch_poster(144),
        fetch_poster(44801),
        fetch_poster(340),
        fetch_poster(163),
        fetch_poster(290),
        fetch_poster(9722),
        fetch_poster(914),
        fetch_poster(155),
        fetch_poster(255709),
        fetch_poster(572154),
        fetch_poster(156),
        fetch_poster(100),
    ]
    selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

    if selectedImageUrl is not None:
        st.image(selectedImageUrl)

if __name__ == "__main__":
    main()


if st.button('Show Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
