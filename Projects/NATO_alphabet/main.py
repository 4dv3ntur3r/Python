import pandas

nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

def generate_phonetic():
    user_input = input("Please enter a word to convert: ").upper()

    try:
        result = [nato_dict[letter] for letter in user_input]
    except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic()
    else:
        print(result)

generate_phonetic()