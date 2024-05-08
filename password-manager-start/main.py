from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate a random password
def generate_password():
    # Define lists of characters, numbers, and symbols
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random letters, symbols, and numbers for the password
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine the generated characters, symbols, and numbers
    password_list = password_letter + password_symbols + password_numbers

    # Shuffle the password characters
    shuffle(password_list)

    # Join the characters to form the password
    password = "".join(password_list)

    # Insert the generated password into the password input field
    password_input.insert(0, password)

    # Copy the password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Function to save the password details
def save():
    # Get the website, email, and password from the input fields
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    # Check if website and password fields are empty
    if len(website) == 0 or len(password) == 0:
        # Show a message box if any field is empty
        messagebox.showinfo(title="Oops", message="You have left some fields empty")
    else:
        # Read a file
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
            #Updating the old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                #Saving updated data
                json.dump(data,data_file, indent=4)
        finally:
            # Clear input fields after saving
             website_input.delete(0, END)
             password_input.delete(0, END)
# ---------------------------- FIND PASSWORD --------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file exists")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= "website", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

    

# ---------------------------- UI SETUP ------------------------------- #
# Setup the user interface
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas to display the lock image
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)  # Position the image
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry()
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

username_input = Entry()
username_input.grid(column=1, row=2, sticky="EW")
username_input.insert(0, "dhananjay@gmail.com")  # Insert default email

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

# Main loop to run the application
window.mainloop()