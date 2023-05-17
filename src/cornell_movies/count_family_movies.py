import pandas as pd
from src.count_words import count_all_words, count_test_words, get_words


def main():
    # path to the csv output of get_family_movies.py
    movie_lines_path = "../../data/cornell_movies/cornell_family_movies_lines.csv"
    movie_lines = pd.read_csv(movie_lines_path)
    movie_lines = movie_lines.dropna()

    total_word_count = count_all_words(movie_lines, 'movies')

    for mc in [True, False]:
        words_df, words_dict = get_words(mc)
        word_counts = count_test_words(movie_lines, words_dict)

        words_df["Movies Count"] = words_df["Word"].map(word_counts)
        words_df["Movies Total Count"] = total_word_count
        words_df["Movies Frequency per 1000 words"] = words_df["Movies Count"].div(words_df["Movies Total Count"]).mul(1000)

        output_path = f"../../output/cornell_movies/{'mc' if mc else 'non_mc'}_cornell_family_movies_counts.csv"
        words_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
