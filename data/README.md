# Data

### Children's Picture Books
We used books that were indentified in the Infant Bookreading Database (Hudson Kam & Matthewson, 2017). This database is available at https://linguistics.ubc.ca/research/.
>Hudson Kam, C. L. & Matthewson, L. (2017). Introducing the Infant Bookreading Database (IBDb). Journal of Child Language, 44, 1289-1308.
### COCA

>Davies, M. (2008-). The Corpus of Contemporary American English (COCA). Available online at https://www.english-corpora.org/coca/ 

Note that some tokens are randomly replaced with the @ symbol upon distribution of the corpus. This may cause counts to vary. 
### Cornell Movie-Dialogs Corpus
The [Cornell Movie-Dialogs Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html) was introduced by Danescu-Niculescu-Mizil & Lee (2011). It can be downloaded using [ConvoKit](https://convokit.cornell.edu/documentation/movie.html). Alternatively, it can be downloaded as text files from [here](https://www.kaggle.com/datasets/rajathmc/cornell-moviedialog-corpus), which is what we used. 
>Danescu-Niculescu-Mizil, C. & Lee, L. (2011). Chameleons in imagined conversations:  A new approach to understanding coordination of linguistic style in dialogs in Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics, ACL 2011.

# Folder Structure
The data should be organized as follows to ensure the scripts run without error. Firstly, the books listed in the Infant Bookreading Database should be transcribed to docx files contained in the children_books directory. Secondly, the COCA data should be structured as illustrated with the `text_fic_jjw`, `text_mag_jgr`, and `text_tvm_nwh` directories containing the text files provided by the distributors of COCA. `sources.txt` is also provided by them. Thirdly, the `movie_lines.txt` and `movie_lines_meta_data.txt` files from the Cornell Movie-Dialogs Corpus download should be positioned as shown.

```.
└── data
    ├── childrens_books
    │   ├── book_1_filename.docx
    │   ├── book_2_filename.docx
    │       .
    │       .
    │       .
    │   └── book_445_filename.docx
    ├── COCA
    │   └── data
    │       ├── coca-text
    │       │   ├── text_fic_jjw
    │       │   ├── text_mag_jgr
    │       │   └── text_tvm_nwh
    │       └── sources.txt
    ├── cornell_movies
    │   └── cornell movie-dialogs corpus
    │       ├── movie_lines.txt
    │       └── movie_titles_metadata.txt
    ├── tests
    │   ├── mc_test_words.csv
    │   └── non_mc_test_words.csv
    └── README.md

 ```
# Tests
These files contain the words from the morphological awareness tests that we analyzed. There are two files: one for multiple choice assessments and one for non-multiple choice assessments. The references provided in these files are author names and year only; full references can be found in the paper.