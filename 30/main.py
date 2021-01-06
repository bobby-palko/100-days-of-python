from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

timer = None

next_word_pair = {}

# -------------------- DATA SETUP -------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

translation_list = data.to_dict(orient="records")


# -------------------- NEW WORD GEN -------------------- #

def is_known():

    translation_list.remove(next_word_pair)
    data = pandas.DataFrame(translation_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global timer, next_word_pair

    if timer:
        window.after_cancel(timer)
    
    next_word_pair = choice(translation_list)
    french_word = next_word_pair.get("French")

    canvas.itemconfig(flashcard, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")

    timer = window.after(3000, flip_card, next_word_pair.get("English"))

# -------------------- SHOW ENGLISH WORD -------------------- #

def flip_card(english_word):

    canvas.itemconfig(flashcard, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")


# -------------------- UI SETUP -------------------- #

window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, font=LANGUAGE_FONT, text="")
word = canvas.create_text(400,263, font=WORD_FONT, text="")

canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()