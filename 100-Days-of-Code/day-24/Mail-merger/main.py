
with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        letter_read = open("./Input/Letters/starting_letter.txt", mode="r")
        name_to = name.rstrip('\n')
        letter_write = open(f"./Output/ReadyToSend/{name_to}.txt", mode="w")
        letter_write.write(letter_read.read().replace("[name]", name_to))
        letter_read.close()
        letter_write.close()
