# 80 Percent Comprehension

A project to use word frequencies of books to create helpful vocabulary lists.

The bs4_to_csv.py script scrapes a html file from Project Gutenburg and turns it into two csv files. The first csv is a filtered word list that will be used to build vocab cards with Merriam Webster Dictionary API definitions. The second csv file also includes less helpful words (such as names, places, etc.). This file is needed for statistical comparisons.

Next the two csv files are analyzed in a Jupyter Notebook. This analysis is used to find the amount of words needed for 80% comprehension of the given text.

The mwd.py script works with the Merriam Webster Dictionary API to retrieve definitions of the words needed for 80% comprehension, and writes them to a new vocab csv file.

The final csv files are then turned into an Anki flashcard desk with the anki.py script.
