from docx import Document
import pandas as pd
from pathlib import Path
from src.count_words import count_all_words, count_test_words, get_words


def get_data_from_files(data_path: Path):
    """
    Get data from a folder of docx files and put it into a pandas dataframe.
    :param data_path: a Path of a folder containing docx files
    :return: a pandas dataframe with columns "title" and "text" containing the info from the files in data_path
    """
    data_files = data_path.glob("*.docx")
    books = []
    for file in data_files:
        text = " ".join([paragraph.text for paragraph in Document(file).paragraphs])
        books.append([file.stem, text])

    books = pd.DataFrame(books, columns=["title", "text"])
    return books


def main():
    data_path = Path("../../data/childrens_books")
    books = get_data_from_files(data_path)
    total_word_count = count_all_words(books, 'movies')

    for mc in [True, False]:
        words_df, words_dict = get_words(mc)
        word_counts = count_test_words(books, words_dict)

        words_df["Books Count"] = words_df["Word"].map(word_counts)
        words_df["Books Total Count"] = total_word_count
        words_df["Books Frequency per 1000 words"] = words_df["Books Count"].div(words_df["Books Total Count"]).mul(1000)

        output_path = f"../../output/childrens_books/{'mc' if mc else 'non_mc'}_childrens_books_counts.csv"
        words_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
