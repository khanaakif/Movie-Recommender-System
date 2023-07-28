# Movie Recommender System

![Picture 1](https://github.com/khanaakif/Movie-Recommender-System/assets/135196262/4b0dae9f-75e2-4428-ac44-4d03d6f04d42)

## Overview

Welcome to the Movie Recommender System! This is a simple and intuitive web application that helps you discover new movies based on your preferences. The system uses collaborative filtering to suggest movies that are similar to the one you select.

## How it Works

1. Select a Movie: Start by using the user-friendly dropdown menu to choose a movie from the vast collection available in our database.

2. Click "Recommend": After selecting a movie, just click the "Recommend" button to get a list of five movie recommendations related to your choice.

3. Explore Recommendations: You will see the top five movie recommendations along with their posters, fetched from The Movie Database API.

## Features

- Interactive UI: The web app is built with Streamlit, providing a seamless and engaging user experience.

- Fast Recommendations: The system uses pre-calculated similarity scores, allowing for quick and efficient movie recommendations.

- Beautiful Posters: Each recommendation comes with an eye-catching movie poster fetched directly from The Movie Database API.

## Getting Started

1. Clone the Repository:
git clone https://github.com/khanaakif/Movie-Recommender-System.git
cd movie-recommender-system

2. Install Dependencies:
Install all the libraries mentioned in the [requirements.txt](https://github.com/khanaakif/Movie-Recommender-System/blob/main/requirements.txt) file with the command `pip install -r requirements.txt`.

3. Run the App:
streamlit run app.py


4. Select a Movie:
   - Use the dropdown menu to choose a movie.
   - Click the "Recommend" button to get your movie recommendations.

## Data Sources

- Movie Data: The movie details and metadata are obtained from The Movie Database (TMDb) API.
- [Dataset Link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/download?datasetVersionNumber=2)

## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## Acknowledgments

We would like to express our gratitude to The Movie Database (TMDb) for providing the movie data and poster images for this project.

## Support and Contribution

If you encounter any issues, have suggestions, or would like to contribute to the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
