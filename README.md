# zipf

A project to use word frequencies of books to create helpful vocabulary lists.

The bs4_to_csv.py scrapes a html file from Project Gutenburg and turns it into two csv files, one that will be used in a Merriam Webster Dictionary API, and one that contains less helpful words (such as names, places, etc.). The second file is needed to help with statistical comparisons.

Next the two csv files are compared (currently in a Jupyter Notebook). This is used to find the number of words needed to have 80% comprehension of the book in question.

The mwd.py script works with the Merriam Webster Dictionary API to retrieve definitions of the words needed for 80% comprehension, and writes them to a csv file.

The final csv files are in a clean form to be used as is or uploaded to an Anki deck. 

https://superuser.com/questions/698902/can-i-create-an-anki-deck-from-a-csv-file/1127023
