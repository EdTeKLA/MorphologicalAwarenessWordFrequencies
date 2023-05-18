import pandas as pd
from count_words import count_all_words, count_test_words, get_words


def main():
    # path to the csv output of get_childrens_texts_COCA.py
    texts = pd.read_csv(f"../data/COCA/childrens_texts_COCA.csv")

    total_word_count = count_all_words(texts, 'COCA')
    for subgenre in ['FIC:Juvenile', 'MAG:Children', 'Movies:Family']:
        print(f'Number of words in {subgenre}: {count_all_words(texts.loc[texts["subgenre_name"]==subgenre], "COCA")}')

    for mc in [True, False]:
        words_df, words_dict = get_words(mc)
        word_counts = count_test_words(texts, words_dict)

        words_df["COCA Count"] = words_df["Word"].map(word_counts)
        words_df["COCA Total Count"] = total_word_count
        words_df["COCA Frequency per 1000 words"] = words_df["COCA Count"].div(words_df["COCA Total Count"]).mul(1000)

        output_path = f"../output/COCA/{'mc' if mc else 'non_mc'}_COCA_counts.csv"
        words_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
