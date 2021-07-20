import pandas as pd

word_dic = {}


def main():
    with open("pnorvig_ngram.txt") as txt:
        for x in range(10000):
            line = txt.readline()
            word, count = line.strip().split('\t')
            word = word.capitalize()
            word_dic[word] = count

    series = pd.Series(word_dic).to_frame()
    pd.DataFrame(series).to_csv('n_gram.csv')


if __name__ == "__main__":
    main()
