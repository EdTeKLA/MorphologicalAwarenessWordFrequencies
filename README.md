# Morphological Awareness Word Frequencies

This repository contains scripts to obtain the frequencies of words from several morphological awareness tests based on their occurrence in English corpora intended for children. 

## Data
[mc_test_words.csv](data/tests/mc_test_words.csv) and [non_mc_test_words.csv](data/tests/non_mc_test_words.csv) contain the lists of words from various morphological awareness tests (multiple choice and non-multiple choice) that are to be counted.

The frequencies of these words were obtained from COCA (juvenile fiction, children's magazines, and family movies only), the Cornell Movie-Dialogs corpus (family movies only), and a collection of children's picture books. These corpora are not included in this repository but instructions for how to access them are included in the [data/README.md](data/README.md).

## Output
The word frequencies for each of the corpora can be found in [output](output). The CHILDES counts are not generated by these scripts.


## Running the Code
The packages in [requirements.txt](requirements.txt) are needed to run the code. They can be installed by running 
`pip install -r requirements.txt` from this directory.

Each python script should be run from the directory it is located in.

The corpora are needed to run the code for counting the words. Follow the instructions in the [data/README.md](data/README.md) to set up the data appropriately. 
### Children's Picture Books
From this directory, run
```
cd src
python3 get_and_count_childrens_books.py
```
  

### COCA
From this directory, run
```
cd src
python3 get_childrens_texts_COCA.py
python3 count_childrens_texts_COCA.py
```

### Cornell Movie-Dialogs Corpus
From this directory, run
```
cd src
python3 get_family_movies.py
python3 count_family_movies.py
```

### Violin Plots
Violin plots can be generated once the frequencies have been obtained from all the corpora. The frequencies are already provided in [output](output) so they can be generated by running the following code from this directory.
```
cd src
python3 combine_counts.py
cd violin_plots
python3 mc_violin_plot.py
python3 non_mc_violin_plot.py
```
