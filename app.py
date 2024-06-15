import streamlit as st
import pickle
import pandas as pd

# Load the movie data and similarity matrix
movies = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Set up the title and description
# Add animated text
st.markdown("<h2 class='moving-text'>🎥 </h2>", unsafe_allow_html=True)
st.title('🎬 Movie Recommender System')
st.markdown("""
    **Welcome to the Movie Recommender System!**  
    *Select a movie from the dropdown list below and click the 'Recommend' button*  
    *to get a list of similar movies.*
""")

# Selectbox for movie selection
selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values,
    key='movie_selection'
)

# Recommendation button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader('Recommended Movies:')
    for movie in recommendations:
        st.write(f"🎥 {movie}")

# Add some spacing and footer
st.markdown("---")
# Add "Developed By" section with increased size
st.markdown("<h2 style='font-size: 24px;'>Developed By ❤️ Pranav!</h2>", unsafe_allow_html=True)


# Add some custom CSS for styling and animation
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #e6f2ff, #ffcccc); /* Light shades of blue and pink */
        color: black; /* Text color black */
        overflow: hidden; /* Disable scrolling */
    }
    .stButton button {
        background-color: #66ff66; /* Light green */
        border: none;
        color: black; /* Text color black */
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #33cc33; /* Darker green on hover */
    }
    .stTitle, .stHeader, .stSubheader, .stMarkdown, .stText {
        color: black; /* Text color black */
        font-family: 'Arial', sans-serif; /* Font family */
    }
    .stTitle {
        font-size: 36px; /* Increase font size for title */
    }
    .stMarkdown {
        font-size: 18px; /* Increase font size for markdown */
    }
    .stSubheader {
        color: white; /* Recommended Movies header color */
    }
    .stSelectbox label {
        font-weight: bold; /* Make Selectbox label bold */
    }

    /* Animation */
    @keyframes moveAnimation {
        0% { transform: translateX(0px); }
        50% { transform: translateX(100px); }
        100% { transform: translateX(0px); }
    }

    .moving-text {
        animation: moveAnimation 3s infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)


