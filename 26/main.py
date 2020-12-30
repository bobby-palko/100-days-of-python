from tkinter import *

def mile_to_km(miles):
    return miles * 1.609344

def update_text():
    km = mile_to_km(float(entry.get()))
    converted_km.config(text=km)

window = Tk()
window.title("Miles to Km Calculator")
window.config(padx=20, pady=20)

# Labels
miles_text = Label(text="Miles")
km_text = Label(text="Km")
equal_text = Label(text="is equal to")
converted_km = Label(text="0")

# entry
entry = Entry(width=10)

# button
button = Button(text="Calculate", command=update_text)

# layout
entry.grid(column=1, row=0)
miles_text.grid(column=2, row=0)
equal_text.grid(column=0, row=1)
converted_km.grid(column=1, row=1)
km_text.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()