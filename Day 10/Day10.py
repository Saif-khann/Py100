'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 8: Basic Calculator Program
-----------------------------------
This program simulates a simple calculator that can perform
addition, subtraction, multiplication, and division operations.
The user can choose an operation, input numbers, and decide
whether to continue calculating with the result or start a
new calculation.
-----------------------------------
'''

import art  # Importing the logo from the art module for display

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract second number from the first
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# Function to divide the first number by the second
def divide(n1, n2):
    return n1 / n2

# Dictionary mapping operation symbols to the corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Main function for the calculator
def calculator():
    print(art.logo)  # Displaying the logo at the start of the calculator

    should_accumulate = True  # Variable to control if we keep using the result for the next calculation
    num1 = float(input("What is the first number: "))  # Asking the user for the first number

    while should_accumulate:  # Continue the loop until the user chooses to stop
        # Displaying available operations to the user
        for symbol in operations:
            print(symbol)

        # Asking the user to pick an operation
        operation_symbol = input("Pick an operation: ")

        # Asking the user for the next number to perform the operation with
        num2 = float(input("What is the next number: "))

        # Performing the chosen operation using the selected function from the dictionary
        answer = operations[operation_symbol](num1, num2)

        # Displaying the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Asking the user if they want to continue, start a new calculation, or stop
        choice = input(f"Type 'y' to continue calculating with {answer}, "
                       f"or type 'n' to start a new calculation, or type 's' to stop: ")

        # If the user wants to continue calculating with the current result
        if choice == "y":
            num1 = answer  # Use the current result for the next calculation
        # If the user wants to start a new calculation
        elif choice == "n":
            should_accumulate = False  # Stop the current loop
            print("\n" * 20)  # Clear screen with new lines
            calculator()  # Restart the calculator for a new calculation
        # If the user wants to stop the calculator
        else:
            should_accumulate = False  # End the loop and stop the calculator
            print("GoodBye!")  # Display goodbye message

# Start the calculator program
calculator()
