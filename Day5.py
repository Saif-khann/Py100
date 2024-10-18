'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
----------------------------------------------
Day 5 Project: Password Generator 🔐
----------------------------------------------
Create a password generator that allows users to customize the length of their password
by specifying how many letters, symbols, and numbers they want in the password.

Description:
1. Greet the user and introduce the password generator program.
2. Ask the user for the number of letters, symbols, and numbers they want in their password.
3. Create an "easy level" password where the order of characters is not randomized.
4. Create a "hard level" password where the characters are randomly shuffled.
5. Display both passwords to the user.

Code starts here...
'''

import random  # Importing the random module for random selection and shuffling

# List of possible letters, numbers, and symbols to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greet the user and explain the purpose of the program
print("Welcome to the PyPassword Generator!")

# Ask the user for the number of letters, symbols, and numbers to include in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level Password (ordered as entered by the user)
password = ""  # Initialize an empty password string

# Add random letters to the password
for char in range(0, nr_letters):
    password += random.choice(letters)

# Add random symbols to the password
for char in range(0, nr_symbols):
    password += random.choice(symbols)

# Add random numbers to the password
for char in range(0, nr_numbers):
    password += random.choice(numbers)

# Display the easy-level password (order of characters not shuffled)
print(f"Easy password: {password}")

# Hard Level Password (characters shuffled randomly)
password_list = []  # Initialize an empty list to store password characters

# Add random letters to the password list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Display the password list before shuffling
print(password_list)

# Shuffle the password list to randomize the order
random.shuffle(password_list)

# Display the shuffled password list
print(password_list)

# Combine the shuffled characters into a final password string
password = ""
for char in password_list:
    password += char

# Display the hard-level password (characters randomly shuffled)
print(f"Your hard password is: {password}")
