# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from make_dir import create_dir
import spacy

nlp = spacy.load("en_core_web_sm")
#-------------------------------------------------------------------------------
# Fill in this section
web_address = "https://www.gutenberg.org/files/1260/1260-h/1260-h.htm"
name = "Jane"
#-------------------------------------------------------------------------------
def spacy_filter(word):
    """Uses spacy to find lemmas of verbs and roots of aux verbs"""
    doc = nlp(word)
    for token in doc:
        if token.pos_ == "VERB":
            return token.lemma_
        elif token.pos_ == "AUX":
            aux_lst = [token for token in doc if token.pos_ == "AUX"]
            return aux_lst[0]
        else:
            return filter(word)

def filter(word):
    """Extra filtering to deal with beginning of sentances, filtering of names, and unicode"""
    if word in ["a", "A", "I", "O", 'The', "Then", "It", "He", "She", "They", "And", "When", "If", "That", "Who", "What", "When", "Where", "Why", "How"]:
        return word
    elif word == word.capitalize() or word == word.upper():
        return ""
    elif len(word) == 1:
        return ""
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
            filtered_word = spacy_filter(word)
            filtered_word = str(filtered_word)
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
    create_dir(name)
    path = create_dir(name)
    # print(path)
    word_dic, filtered_word_dic = create_dicts()
    dict_to_csv(word_dic, filtered_word_dic, path)
