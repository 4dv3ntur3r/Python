import pandas

nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

user_input = input("Please enter a word to convert: ").upper()
result = [nato_dict[letter] for letter in user_input]

print(result)