from tkinter import *


def miles_to_kilometers():
    miles = float(mile_input.get())
    kilometers = miles * 1.60934
    kilometer_label.config(text=f"{kilometers:.2f} Km")

window = Tk()
window.title("Mile to Killo Converter")
window.minsize(width=500, height=300)       

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)    




mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)    



is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1) 


kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)   



calculate_button = Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(column=1, row=2)




















window.mainloop()