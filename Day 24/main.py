'''
✉️ (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 24 Project: Personalized Birthday Invitations
-----------------------------------
Description:
This script reads a starting letter template and a list of invited names, then generates personalized invitation
letters for each person. The generated letters are saved in the "Output/ReadyToSend" directory. The names are
read from a file in the "Input/Names" directory, and the template is located in the "Input/Letters" directory.
Each name in the list is used to replace the placeholder "[name]" in the template, creating a unique letter.
-----------------------------------
'''

# Placeholder to be replaced in the letter template
PLACEHOLDER = "[name]"

# Read the list of invited names from the "invited_names.txt" file
with open(r"./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # Read all lines into a list

# Read the starting letter template from "starting_letter.txt"
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # Read the entire content of the letter

    # Loop through each name in the names list
    for name in names:
        stripped_name = name.strip()  # Remove any leading or trailing whitespace from the name
        # Replace the placeholder with the current name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        # Save the personalized letter to the "Output/ReadyToSend" directory
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  # Write the new letter to a file
