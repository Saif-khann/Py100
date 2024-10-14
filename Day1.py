# 🐍 (Py100: 100 Days of Python Challenge)
# Author: Saif Khan
# ----------------------------------------------
# Day 1 Project: Band Name Generator 🎸
# ----------------------------------------------
# Create a fun greeting program that generates a unique band name for the user.

# Description:
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in and store it in a variable.
# 3. Ask the user for the name of a pet and store it in a variable.
# 4. Combine the name of their city and pet and show them their band name.

# Note: Make sure the input cursor shows on a new line.

# Example Output:
# "Your band name could be: New York Fluffy"

# Code Starts here...

# Display the Generator name
print("Welcome to the Band Name Generator")

# Get the name of the city the user grew up in
cityName = input("Which city did you grow up in?\n")

# Get the name of the user's pet
petName = input("What's the name of your pet?\n")

# Display the generated band name
print("Your band name could be: " + cityName + " " + petName + "!")