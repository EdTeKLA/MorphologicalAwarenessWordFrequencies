import pandas as pd
import re
import string
from tqdm import tqdm


def get_words(mc: bool):
    """
    :param mc: specifies whether to get the multiple choice test words or non-multiple choice assessment words
    :return: dict and pandas dataframe with columns 'Reference', 'Item number', 'Type', and 'Word'
    """
    data_path = f"../data/tests/{'mc' if mc else 'non_mc'}_test_words.csv"

    words_df = pd.read_csv(data_path)
    words_dict = {word: 0 for word in set(words_df["Word"])}

    return words_df, words_dict


def count_all_words(texts: pd.DataFrame, source: str):
    """
    This function counts the words in texts based on the formatting of the source. Only tokens containing letters,
    numbers, and apostrophes are counted as words. Contractions are counted as one word.
    :param texts: a pandas dataframe that must contain a column named "text" that stores the texts from the source
    :param source: a str specifying the source of the texts ("COCA", "movies", or "books").
                   This parameter is used to tailor the processing of the texts based on the formatting of the
                   original source.
    :return count: an int storing the total count of all words in the texts
    """
    count = 0
    if source == "COCA":
        for index, row in tqdm(texts.iterrows()):
            text = row["text"]
            tokens = text.split()
            for token in tokens:
                # COCA usually has contractions as separate tokens: can't --> can n't or I'll --> I 'll
                # so counting only alphanumeric tokens will count these words as a single word
                if token.isalnum():
                    count += 1
                elif token.replace('-', '').isalnum():  # hyphenated words should be counted as a single word
                    count += 1
                # words that contain an apostrophe such as o'clock of Smiths' are counted here
                # the additional conditions avoid double counting contractions such as: 'll and n't
                elif token.replace("'", '').isalnum() and token[0] != "'" and token[0:2] != "n'":
                    count += 1

    elif source == "movies":
        for index, row in tqdm(texts.iterrows()):
            text = row["text"]
            # some contractions are separated and some are not. this handles situations like can ' t --> cant
            text = text.replace(" ' ", "")
            # remove all punctuation so that can't --> cant, ill-fated --> illfated so these are counted as one word
            for punctuation in string.punctuation + "…" + "”" + "“" + "’" + "—" + "‘" + "–":
                text = text.replace(punctuation, '')
            tokens = text.split()

            for token in tokens:
                if token.isalnum():
                    count += 1

    elif source == "books":
        for index, row in tqdm(texts.iterrows()):
            text = row["text"]
            # remove all punctuation so that can't --> cant, ill-fated --> illfated so these are counted as one word
            for punctuation in string.punctuation + "…" + "”" + "“" + "’" + "—" + "‘" + "–":
                text = text.replace(punctuation, '')
            tokens = text.split()

            for token in tokens:
                if token.isalnum():
                    count += 1
    return count


def count_test_words(texts: pd.DataFrame, words_dict: dict):
    """
    This function counts the test words in texts.
    :param texts: a pandas dataframe that must contain a column named "text" that stores the texts from the source
    :param words_dict: a dict that stores the test words as keys and word counts as values (all zero to start).
    :return words_dict: the updated version of word_dict with the word counts as values
    """
    for index, row in tqdm(texts.iterrows()):
        text = str(row["text"]).replace("'", "").lower()
        for word in words_dict:
            words_dict[word] += len(re.findall(r'\b' + word + r'\b', text))

    return words_dict
