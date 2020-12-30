import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("enter a word: ").upper()

nato_word = [nato_dict.get(letter) for letter in word]

print(nato_word)