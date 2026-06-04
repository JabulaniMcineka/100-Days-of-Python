from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Entry
entry = Entry(width=30)
entry.grid(column=1, row=0)

# Button action
def action():
    print(entry.get())

# Button
button = Button(text="Click Me", command=action)
button.grid(column=2, row=0 )
button.config(padx=50, pady=50) 
window.mainloop()