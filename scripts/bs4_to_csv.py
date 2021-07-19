# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

#-------------------------------------------------------------------------------
# Fill in this section
web_address = "https://www.gutenberg.org/files/1260/1260-h/1260-h.htm"
name = "Jane"
#-------------------------------------------------------------------------------
def make_dir(name):
    parent = os.path.dirname(os.getcwd())
    path = os.path.join(parent, name)
    if not os.path.exists(path):
        os.mkdir(os.path.join(path))
    return path

def filter(word):
    if word.endswith('ies') or word.endswith('ied'):
        word = word[:-3]+ "y"
        return word
    elif word in ["a", "A", "I", "O", 'The', "Then", "It", "He", "She", "They", "And", "When", "If", "That", "Who", "What", "When", "Where", "Why", "How"]:
        return word
    elif word == word.capitalize() or word == word.upper():
        return ""
    elif len(word) == 1:
        return ""
    elif word.endswith("dn"):
        return word[:-1]
    elif word.endswith("n't"):
        return word[:-3]
    elif word.endswith("n'"):
        return word[:-2]
    elif word.endswith("s") and not word.endswith("as") and not word.endswith("is") and not word.endswith("ys") and not word.endswith("es") and not word.endswith("ss") and not word.endswith("us") and not word.endswith("os"):
        return word[:-1]
    elif word.endswith("d've"):
        return word[:-3]
    elif word.endswith('â') or word.endswith('Â'):
        return word[:-1]
    else:
        return word

# Uses requests to read the html and beautiful soup to parse it
def create_dicts():
    source = requests.get(web_address).text
    soup = BeautifulSoup(source, "lxml")

    matches = soup.find_all('p')

    word_dic = {}
    filtered_word_dic = {}
    word_lst = []
    for match in matches:
        #print(tag)
        m = match.text
        word_lst = re.findall("[\w]+", m) #creates filtered word dicionary
        for word in word_lst:
            word = word.replace("-_;:", "").strip()
            filtered_word = filter(word)
            filtered_word = filtered_word.capitalize()
            if filtered_word == "":
                continue
            filtered_word_dic[filtered_word] = filtered_word_dic.get(filtered_word, 0) + 1

        for word in word_lst: #creates unfiltered word dictionary
            word = word.replace("-_;:", "").strip()
            word = word.capitalize()
            if word == "" or word.endswith('Â'):
                continue
            word_dic[word] = word_dic.get(word, 0) + 1

    return word_dic, filtered_word_dic

def dict_to_csv(word_dic, filtered_word_dic, path):
    series = pd.Series(word_dic).to_frame()
    pd.DataFrame(series).to_csv(f'{path}/{name}.csv')
    filtered_series = pd.Series(filtered_word_dic).to_frame()
    pd.DataFrame(filtered_series).to_csv(f'{path}/{name}_filtered.csv')

if __name__ == "__main__":
    make_dir(name)
    path = make_dir(name)
    # print(path)
    word_dic, filtered_word_dic = create_dicts()
    dict_to_csv(word_dic, filtered_word_dic, path)
