# Libraries
from tkinter import *

# Colors
WHITE = "#F9F9F9"
RED = "#c0392b"

# Font Family
FONT = ("Raleway", 9, "bold")


# Add passwords to data.txt
def add_password():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    with open("data.txt", mode="a") as data:
        data.write(f"{website} | {email_username} | {password}\n")
    website_input.delete(0, END)
    password_input.delete(0, END)


# Root object definition
root = Tk()
root.title("Password Manager")
root.config(padx=40, pady=40, bg=WHITE)
root.resizable(width=False, height=False)

# Canvas object definition
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Widgets
# Website label
website_label = Label(text="Website:", font=FONT, bg=WHITE, fg=RED)
website_input = Entry(width=44, highlightbackground=RED, highlightthickness=1, font=FONT)
website_input.focus()

# Email/Username label
email_username_label = Label(text="Email/Username:", font=FONT, bg=WHITE, fg=RED)
email_username_input = Entry(width=44, highlightbackground=RED, highlightthickness=1, font=FONT)
email_username_input.insert(0, "shuvonasir028@gmail.com")

# Password label
password_label = Label(text="Password:", font=FONT, bg=WHITE, fg=RED)
password_input = Entry(width=25, highlightbackground=RED, highlightthickness=1, font=FONT)
pass_gen_button = Button(text="Generate Password", font=("Raleway", 9, "bold"), fg="white", bg=RED)
add_button = Button(text="Add Password", font=("Raleway", 9, "bold"), bg=RED, fg="white", width=44,
                    command=add_password)

# Grids
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2, sticky="e", pady=2)
email_username_label.grid(row=2, column=0)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="e", pady=2)
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1)
pass_gen_button.grid(row=3, column=2, sticky="e", pady=2)
add_button.grid(row=4, column=0, columnspan=3, sticky="e", pady=2)

# Root mainloop
root.mainloop()
