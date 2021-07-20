import configparser
import requests
import csv
import re
from make_dir import create_dir

# ------------------------------------------------------------------------------
# Fill in this area
csv_name = "nonsense"
word_lst = ['Break', 'Rise', 'Have', 'Meet', 'Keep', 'Ring', 'Forget', 'Drink',
            'Become']
# ------------------------------------------------------------------------------
unparsed = []
cfg = configparser.ConfigParser()
cfg.read('comprehension.cfg')

app_key = cfg.get('KEYS', 'api_key', raw='')


def normalize(phrase):
    """normalizes messy json definition into a string"""
    # Filter out extra unicode nonsense
    key = r"([\d\w +-.''"",?!\(\):;]*){[\w/]*}([\d\w +-.''"",?!\(\);:]*)"
    str_lst = re.findall(key, phrase)

    if str_lst == []:
        return phrase
    else:
        str = ''
        for i, x in str_lst:
            str += i
            str += x
        return str


def main():
    """Json into vocab csv files, else returns unparsed words in a list"""
    path = create_dir(csv_name)
    with open(f'{path}/{csv_name}.csv', 'a') as file:
        writer = csv.writer(file)
        for word in word_lst:
            url = 'https://www.dictionaryapi.com/api/v3/references/learners/json/' + word + '?key=' + app_key

            try:
                r = requests.get(url)
                j = r.json()
                definition = normalize(j[0]['meta']['app-shortdef']['def'][0])
                pos = j[0]['meta']['app-shortdef']['fl']
                writer.writerow([word, pos, definition])

            except:
                unparsed.append(word)
    return unparsed


if __name__ == "__main__":
    unparsed = main()
    print(unparsed)
