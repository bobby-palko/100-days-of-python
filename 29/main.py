from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]

    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    new_data = {
        site: {
            "email": email,
            "password": password,
        }
    }

    if not site or not password or not email:
        messagebox.showwarning(title="Oops!", message="Please make sure to fill out all fields!")
    
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"Email/Username: {email}\nPassword: {password}\nIs this correct?")

        if is_ok:

            try:
                with open("data.json", "r") as file:
                    # read the old data
                    data = json.load(file) 

            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    #saving updated data
                    json.dump(new_data, file, indent=2)

            else:
                # update with new data
                data.update(new_data)

                with open("data.json", mode="w") as file:
                    #saving updated data
                    json.dump(data, file, indent=2)

            finally:
                site_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    site = site_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if site in data:
            site_info = data[site]
            messagebox.showinfo(title=site, message=f"Email/Username: {site_info.get('email')}\nPassword: {site_info.get('password')}")

        else:
            messagebox.showwarning(title="No Match", message=f"No details for {site} exist.")
            


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

canvas.grid(column=1, row=0)

site_label = Label(text="Website:")
site_label.grid(column=0, row=1)

site_entry = Entry(width=18)
site_entry.grid(column=1, row=1)
site_entry.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=14, command=password_gen)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()