from tkinter import *
from tkinter import messagebox
import pyperclip
import json
YELLOW = "#f7f5dd"
# BUTTON  #


def search():
    website = website_entry.get()
    try:
        with open('saved.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="NoData", message="No data file found!")
    if website_entry.get() in data.keys():
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\n password: {password}")
    else:
        messagebox.showerror(title="Ooops", message="there is no website with this name!")



# PASSWORD GEN #
import random
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    new_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    new_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = new_symbols + new_letters + new_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# SAVE  #


def write():
    new_data = {
        website_entry.get(): {
            "email": user_entry.get(),
                "password": password_entry.get(),
        }
    }
    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror(title="Ooops", message="don't leave fields empty!")
    else:
        try:
            with open('saved.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('saved.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('saved.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# UI #
window = Tk()
window.title("Pass manager")
window.minsize(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.create_image(120, 120, image=pass_img)
canvas.grid(column=1, row=0)

website_entry = Entry(width=35)
website_entry.get()
website_entry.grid(column=1, row=1, columnspan=2, pady=5)
website_entry.focus()

user_entry = Entry(width=35)
user_entry.get()
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "rayman507@gmail.com")


password_entry = Entry(width=18)
password_entry.get()
password_entry.grid(column=1, row=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

pass_button = Button(text="Generate password", command=password_gen)
pass_button.grid(column=3, row=3)
add_button = Button(width=36, text="Add", command=write)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=3, row=1)



window.mainloop()