import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers) ]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
             }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!', message="please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data= json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clear inputs
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found')
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n Password: {data[website]['password']}")

        else:
            messagebox.showerror(title="Not Found", message=f"No details for '{website}' exist.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady= 50)
window.title('Password manager')

canvas = Canvas(height= 200, width= 200)
logo = PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image= logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3,column=0)


website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0, 'madhumm@gamil.com')
password_input = Entry(width=35)
password_input.grid(row=3,column=1,columnspan=2)

generate_password_button = Button(text='Generate Password',width=20, command=generate_password)
generate_password_button.grid(row=3, column=3)
search_button = Button(text='Search', width=20, command=find_password)
search_button.grid(row=1, column=3)


add_button = Button(text='Add', width=36, command= save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()