from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from  random import choice, randint, shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password,}}

    if len(website) == 0 or len(email) == 0:

        messagebox.showinfo(title="Oops", message="Please make sure you didn't left any files empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

""" ------------------------------------------------------------------------------"""

def find_pass():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
            website_input.delete(0, END)

        else:
            messagebox.showinfo(title="Error", message=f"No data for this website: {website} exist")



# ---------------------------- GUI SETUP ------------------------------- #

window = Tk()
window.title("MY PASS")
window.config(padx=20, pady=20, highlightthickness=0)


canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=my_img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)
email_user_l = Label(text="Email/Username:")
email_user_l.grid(column=0, row=2)
password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)
email_user_input = Entry(width=35)
email_user_input.insert(0, "name@gmail.com")
email_user_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)


add_b = Button(text="Add", width=35, command= save)
add_b.grid(column=1, row=4, columnspan=2)

generate_pass_b = Button(text="Generate password", command= generate_password)
generate_pass_b.grid(column=2, row=3)



search_b = Button(text="Search", width=15, command=find_pass)
search_b.grid(column=2, row=1)



window.mainloop()