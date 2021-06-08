import genanki
import random
import csv

file = "Alice/Alice_vocab.csv"
Deck_name = "Alice"
Deck_id = random.randrange(1 << 30, 1 << 31)
ct = 1

def main():
    ct = 1
    my_deck = genanki.Deck(
     Deck_id,
     Deck_name)

    with open(file, newline='') as csvfile:
        line = csv.reader(csvfile, quotechar='|')
        for line in csvfile:
            lis= line.split(",")
            word = lis[0]
            pos = lis[1]
            definition = lis[2]

            my_model = genanki.Model(
              random.randrange(1 << 30, 1 << 31),
              'Simple Model',
              fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
              ],
              templates=[
                {
                  'name': 'Card {}'.format(ct),
                  'qfmt': '{{Question}}',
                  'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
              ])

            my_note = genanki.Note(
              model=my_model,
              fields=['{}: {}'.format(word, pos), '{}'.format(definition)])

            my_deck.add_note(my_note)
            ct += 1

    genanki.Package(my_deck).write_to_file('{}.apkg'.format(Deck_name))

if __name__ == "__main__":
    main()


# with open(file, newline='') as csvfile:
#     line = csv.reader(csvfile, quotechar='|')
#     for line in csvfile:
#         lis= line.split(",")
#         print(lis[0], lis[2])
