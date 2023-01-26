from tkinter import *
import string
import random
import pyperclip








#UI setup
window = Tk()
window.title("Password manager")
window.config(pady = 20)


canvas = Canvas(width = 200, height = 200 , highlightthickness=0)
password_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = password_image)
canvas.grid(row = 0, column = 1)

website = Label(text="Website:", width=20, height=5)
website.grid(row=2, column=0)
website.focus()

email = Label(text = "Email/Username:", width=20, height=5)
email.grid(row=3, column=0)

password = Label(text = "Password:", width=40, height=5)
password.grid(row=4, column=0 )

#entries

website_entry = Entry(width = 35)
website_entry.grid(row = 2 , column = 1,columnspan = 2)

email_entry = Entry(width = 35)
email_entry.grid(row = 3,column = 1, columnspan = 2)

password_entry = Entry(width = 21)
password_entry.grid(row= 4,column = 1)

def add_data():
    website_info = website_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()

    f = open("data.txt", "a")
    f.write(f"{website_info} | {email_info} | {password_info}\n")

    f.close()

    #open and read the file after the overwriting:
    f = open("data.txt", "r")


def generate_password():
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    punctuation = list(string.punctuation)
    numbers = list(string.digits)
    letters = list(string.ascii_letters)
    password = ""
    for i in range(3):
        password_letter = random.choice(alphabet_lower)
        password += password_letter

        password_upper = random.choice(alphabet_upper)
        password += password_upper

        password_punctuation = random.choice(punctuation)
        password += password_punctuation

        password_number = random.choice(numbers)
        password += password_number


    password_entry.insert(0,password)
    pyperclip.copy(password)
    print(password)


#buttons
generate = Button(text="Generate",command = generate_password)
generate.grid(row = 4 , column = 2 )

add = Button(width =36 ,text = "ADD",command = add_data )
add.grid(column = 1, row = 5 , columnspan = 2)

#upload data




window.mainloop()