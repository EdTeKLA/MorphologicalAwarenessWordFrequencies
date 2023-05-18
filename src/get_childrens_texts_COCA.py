from pathlib import Path
import pandas as pd
import re
from tqdm import tqdm


def get_sources(sources_path: Path) -> pd.DataFrame:
    """
    Read the sources into pandas dataframe.
    :param sources_path: a Path to the text file containing the info for the COCA sources
    :return: a pandas dataframe with the columns "textID", "year", "genre", "subgenre", "source", and "title"
    """
    return pd.read_csv(sources_path, sep='\t', names=['textID', 'year', 'genre', 'subgenre', 'source', 'title'],
                       encoding='unicode_escape', on_bad_lines='skip')


def get_data(genres: dict, sources: pd.DataFrame) -> pd.DataFrame:
    """
    Get COCA data for the specified genres and put it into a pandas dataframe.
    :param genres: a dict of the format {genre (str): [subgenre_code (int), path_to_COCA_texts (Path)]}
    :param sources: a pandas dataframe with the source information
    :return: a pandas dataframe with columns "file_name", "textID", "subgenre_name", "subgenre_code", "year", "text"
    containing the COCA texts for the specified genres specified.
    """
    textID_pattern = r"@@([0-9]+)\s"
    text_info = []
    for subgenre_name, info in genres.items():
        subgenre_code = info[0]
        data_path = info[1]
        text_files = data_path.glob('*.txt')
        for file in tqdm(text_files):
            with open(file) as f:
                lines = f.readlines()
            for line in lines:
                textID = re.findall(textID_pattern, line)
                if textID:
                    textID = int(textID[0])
                    if textID in sources["textID"].values:
                        subgenre = sources[sources.textID == textID].subgenre.iloc[0]
                        if subgenre == subgenre_code:
                            year = sources[sources.textID == textID].year.iloc[0]
                            text_info.append([str(file.name), textID, subgenre_name, subgenre_code, year, line.lower()])

    texts = pd.DataFrame(text_info,
                         columns=["file_name", "textID", "subgenre_name", "subgenre_code", "year", "text"])
    return texts


def main():
    genres = {'FIC:Juvenile': [117, Path("../data/COCA/data/coca-text/text_fic_jjw")],
              'MAG:Children': [132, Path("../data/COCA/data/coca-text/text_mag_jgr")],
              'Movies:Family': [192, Path("../data/COCA/data/coca-text/text_tvm_nwh")]}

    sources_path = Path("../data/COCA/data/sources.txt")
    sources = get_sources(sources_path)

    texts = get_data(genres, sources)
    texts.to_csv(Path(f"../data/COCA/childrens_texts_COCA.csv"))


if __name__ == "__main__":
    main()
