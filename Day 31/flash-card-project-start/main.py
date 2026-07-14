from tkinter import *
from tkinter import messagebox
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


data = pd.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day 31/flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flash_card_canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file= "Day 31/flash-card-project-start/images/card_front.png")
flash_card_canvas.create_image(400, 263, image=card_front_img)
flash_card_canvas.create_text(400, 150, text="Title",font=("arial", 48, "italic"))
flash_card_canvas.create_text(400, 263, text="word",font=("arial", 68, "bold"))
flash_card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file = "Day 31/flash-card-project-start/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)


check_image =  PhotoImage(file="Day 31/flash-card-project-start/images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)


flash_card_canvas = Canvas(width=800, height=526)
data_file = pd.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
words = data_file.to_dict(orient="records")
random_words = random.choice(words)
print(random_words["French"])
print(random_words["English"])


flash_card_canvas.itemconfig(random_words, Text= "French")
flash_card_canvas.itemconfig(random_words, Text=random_words["English"])








window.mainloop()
