"""Utility helpers for interacting with the MovieLens benchmark datasets."""

import requests
import zipfile
import io
import pandas as pd


def load_movielens_data():
    """Download and load the MovieLens "latest small" dataset as DataFrames.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
            Three dataframes representing movies, ratings, and tags files
            from the MovieLens "ml-latest-small" release.
    """
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    with zip_file.open("ml-latest-small/movies.csv") as f:
        movies = pd.read_csv(f)
    
    with zip_file.open("ml-latest-small/ratings.csv") as f:
        ratings = pd.read_csv(f)

    with zip_file.open("ml-latest-small/tags.csv") as f:
        tags = pd.read_csv(f)

    return movies, ratings, tags
