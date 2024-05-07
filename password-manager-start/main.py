from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate a random password
def generate_password():
    # Define lists of characters, numbers, and symbols
    letters = ['a', 'b', 'c', ..., 'Z']
    numbers = ['0', '1', '2', ..., '9']
    symbols = ['!', '#', '$', ..., '+']

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

    # Check if website and password fields are empty
    if len(website) == 0 or len(password) == 0:
        # Show a message box if any field is empty
        messagebox.showinfo(title="Oops", message="You have left some fields empty")
    else:
        # Ask for confirmation to save the details
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: \n Email: {email} \nPassword: {password} \n Is it okay to save")
                                                                                                                
        if is_ok:
            # Write the details to a file
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                # Clear input fields after saving
                website_input.delete(0, END)
                password_input.delete(0, END)

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

# Main loop to run the application
window.mainloop()