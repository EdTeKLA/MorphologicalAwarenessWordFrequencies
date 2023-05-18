import pandas as pd
from pathlib import Path


def convert_text_to_list(genres_text: str):
    """
    Converts a string representation of a list to a python list
    :param genres_text: a str in the format ['word_1', 'word_2', 'word_3', ..., 'word_n']
    :return: a list
    """
    return genres_text.strip('][').replace("'", "").split(', ')


def find_movies(genre: str, meta_data: pd.DataFrame):
    """
    Finds the metadata for movies of a specified genre.
    :param genre: the genre of movie that you want to find
    :param meta_data: a pandas dataframe with the columns 'movieID', 'movie_title', 'movie_year', 'IMDB_rating',
    'no_IMBD_votes', 'genres'
    :return: a pandas dataframe containing the metadata of movies of the selected genre
    """
    movies_meta_data = []
    for index, row in meta_data.iterrows():
        if genre in convert_text_to_list(row['genres']):
            movies_meta_data.append([row['movieID'],
                                     row['movie_title'],
                                     row['movie_year'],
                                     row['IMDB_rating'],
                                     row['no_IMBD_votes'],
                                     row['genres']])
    movies_meta_data = pd.DataFrame(movies_meta_data,
                                    columns=['movieID', 'movie_title', 'movie_year', 'IMDB_rating', 'no_IMBD_votes',
                                             'genres'])
    return movies_meta_data


def get_movie_lines(meta_data, movie_lines):
    """
    Get the movie lines for movies in meta_data
    :param meta_data: a pandas dataframe with the columns 'movieID', 'movie_title', 'movie_year', 'IMDB_rating',
    'no_IMBD_votes', 'genres'
    :param movie_lines: a pandas dataframe with the columns 'lineID', 'characterID', 'movieID', 'character_name', 'text'
    :return: a pandas dataframe of the movie lines for movies in the meta_data dataframe
    """
    selected_movie_lines = []
    for _, meta_data_row in meta_data.iterrows():
        for _, movie_lines_row in movie_lines.iterrows():
            movieID = meta_data_row['movieID']
            if movieID == movie_lines_row['movieID']:
                selected_movie_lines.append([movie_lines_row['lineID'],
                                             movie_lines_row['characterID'],
                                             movie_lines_row['movieID'],
                                             meta_data_row['movie_year'],
                                             movie_lines_row['character_name'],
                                             movie_lines_row['text']])
    selected_movie_lines = pd.DataFrame(selected_movie_lines,
                                        columns=['lineID', 'characterID', 'movieID', 'movie_year', 'character_name',
                                                 'text'])
    return selected_movie_lines


def main():
    meta_data_path = Path("../data/cornell_movies/cornell movie-dialogs corpus/movie_titles_metadata.txt")
    movie_lines_path = Path("../data/cornell_movies/cornell movie-dialogs corpus/movie_lines.txt")

    meta_data = pd.read_csv(meta_data_path, sep=' \+\+\+\$\+\+\+ ', engine='python', encoding='unicode_escape',
                            names=['movieID', 'movie_title', 'movie_year', 'IMDB_rating', 'no_IMBD_votes', 'genres'])
    movie_lines = pd.read_csv(movie_lines_path, sep=' \+\+\+\$\+\+\+ ', engine='python', encoding='unicode_escape',
                              names=['lineID', 'characterID', 'movieID', 'character_name', 'text'])

    family_movies_meta_data = find_movies('family', meta_data)
    family_movies_lines = get_movie_lines(family_movies_meta_data, movie_lines)

    family_movies_meta_data.to_csv(Path("../data/cornell_movies/cornell_family_movies_meta_data.csv"), index=False)
    family_movies_lines.to_csv(Path("../data/cornell_movies/cornell_family_movies_lines.csv"), index=False)


if __name__ == "__main__":
    main()
