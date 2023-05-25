import pandas as pd
import numpy as np
import re
import string
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


def get_dict(file_name):
    """""This function returns the english to french dictionary given a 
    file where the each column corresponds to a word.
    Check out the files this function takes in your workspace."""""

    etof = {}  # Creating the dictionary to store English and corresponding the french word
    my_file = pd.read_csv(file_name, delimiter=' ')
    for i in range(len(my_file)):
        en_word = my_file.loc[i][0]
        fr_word = my_file.loc[i][1]
        etof[en_word] = fr_word
    return etof

def consine_similarity(A,B):
    cos=-10
    dot=np.dot(A,B)
    A_mod=np.linalg.norm(A)
    B_mod=np.linalg.norm(B)
    cos=dot/(A_mod*B_mod)
    return cos


def hello():
    print("Hello")

hello()
print("Hello world")