from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#fff"
FONT_NAME = "Ariel"
words_to_learn = {}
random_word = {}

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


# Random Word generation
def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words_to_learn)
    canvas.itemconfig(word, text=random_word['French'], fill="#000")
    canvas.itemconfig(language_title, text="French", fill="#000")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_title, text="English", fill=WHITE)
    canvas.itemconfig(word, text=random_word["English"], fill=WHITE)
    canvas.itemconfig(canvas_img, image=card_back_img)


def remove_from_list():
    words_to_learn.remove(random_word)
    next_card()
    data = pd.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=FALSE)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

# To get the image to the center of the container we use half of the container width and half of container (Canvas)
# height
canvas_img = canvas.create_image(400, 263, image=card_front_img)
language_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=remove_from_list)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
