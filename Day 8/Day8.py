'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 8: Caesar Cipher Project
-----------------------------------
This project implements the Caesar Cipher, a simple encryption technique used in the past.
It shifts each letter of the text by a certain number of positions in the alphabet. 
The user can choose to either encode (encrypt) or decode (decrypt) a message. 
The shift is specified by the user. 
Special characters and spaces are not shifted and remain the same.
-----------------------------------
'''

import art

# Print the logo for the Caesar Cipher (stored in an external file `art.py`)
print(art.logo)

# Alphabet list to reference positions for shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Define the Caesar cipher function to encode or decode the text based on shift
def caesar(original_text, shift_amount, encode_or_decode):
    # Initialize an empty string to store the final encoded or decoded text
    output_text = ""
    
    # Reverse the shift if decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each letter in the original text
    for letter in original_text:
        
        # If the character is not in the alphabet (e.g., space or punctuation), add it without shifting
        if letter not in alphabet:
            output_text += letter
        else:
            # Get the new shifted position in the alphabet list, wrapping around with modulo
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            # Add the shifted letter to the output string
            output_text += alphabet[shifted_position]
    
    # Print the final encoded or decoded result
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Flag to keep the game running until the user chooses to stop
should_continue = True

# Main loop of the program
while should_continue:

    # Ask the user whether they want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Ask for the message to be encoded/decoded
    text = input("Type your message:\n").lower()

    # Ask for the shift amount
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function to process the message
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if the user wants to restart the program or end it
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    
    # If user types "no", set the flag to False and exit the loop
    if restart == "no":
        should_continue = False
        print("Goodbye")
