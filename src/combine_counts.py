import pandas as pd


def main():
    for mc in [True, False]:
        data_paths = [f"../output/childrens_books/{'mc' if mc else 'non_mc'}_childrens_books_counts.csv",
                      f"../output/COCA/{'mc' if mc else 'non_mc'}_COCA_counts.csv",
                      f"../output/cornell_movies/{'mc' if mc else 'non_mc'}_cornell_family_movies_counts.csv",
                      f"../output/CHILDES/{'mc' if mc else 'non_mc'}_CHILDES_counts.csv"
                      ]

        df = pd.read_csv(data_paths[0])
        for data_path in data_paths[1:]:
            df = df.merge(pd.read_csv(data_path), on=["Reference", "Item number", "Type", "Word"])

        frequency_columns = ["Books Frequency per 1000 words",
                             "COCA Frequency per 1000 words",
                             "Movies Frequency per 1000 words",
                             "CHILDES Frequency per 1000 words"
                             ]
        df["Average Frequency per 1000 Words"] = df.loc[:, frequency_columns].mean(axis=1)

        output_path = f"../output/all/{'mc' if mc else 'non_mc'}_counts.csv"
        df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
