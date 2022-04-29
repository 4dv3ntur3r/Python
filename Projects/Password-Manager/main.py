from tkinter import *
from tkinter import messagebox
import random
import json

# use to put text directly into clip board
import pyperclip

WHITE = "#fff"

def search_website():

    try:
        with open("data.json", 'r') as file:
            # Load Json data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Info", message=f"No Data file found.")
    else:
        key = website_entry.get()

        if key in data.keys():
            print(data[key]['email'])
            messagebox.showinfo(title=f"Login info on {key}", message=f"Email : {data[key]['email']} \n "
                                     f"Password : {data[key]['password']}")
        else:
            messagebox.showinfo(title=f"Login info", message=f"No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():
    website_name = website_entry.get()
    username = email_or_username_entry.get()
    password = password_entry.get()

    # to put data into a Json file
    new_data = {
        website_name: {
            "email" : username,
            "password": password,
        }
    }

    print(len(website_name) <= 0 and len(username) <= 0 and len(password) <= 0)

    if len(website_name) <= 0 or len(username) <= 0 or len(password) <= 0:
        messagebox.showwarning(title="Oops", message="Don't leave any empty areas.")
    else:
        is_okay = messagebox.askokcancel(title="Title",
                                         message=f"These are the detailed entered: \nWebsite: {website_name} "
                                                 f"\nEmail: {username} \nPassword: {password} \nis it ok to save? ")

        if is_okay:
            try:
                with open("data.json", 'r') as file:
                    # Load Json data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                # update json data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Write to a Json file
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_lable = Label(text="Website: ")
website_lable.grid(column=0, row=1)

email_or_username_lable = Label(text="Email/Username: ")
email_or_username_lable.grid(column=0, row=2)

password_lable = Label(text="Password: ")
password_lable.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1)
website_entry.focus()

email_or_username_entry = Entry(width=39)
email_or_username_entry.grid(column=1, row=2, columnspan=2)
email_or_username_entry.insert(0, "lasantha@example.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

search_btn = Button(text="Search", width=14, command=search_website)
search_btn.grid(column=2, row=1)

gen_pass_btn = Button(text="Generate Password!", command=password_generator)
gen_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=add_to_file)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
