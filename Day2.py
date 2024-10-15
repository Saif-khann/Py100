# 🐍 (Py100: 100 Days of Python Challenge)
# Author: Saif Khan
# ----------------------------------------------
# Day 2 Project: Tip Calculator 💸
# ----------------------------------------------
# Create a simple tip calculator that helps users calculate how much each person should pay when splitting a bill.

# Description:
# 1. Greet the user and introduce the tip calculator program.
# 2. Ask the user for the total bill amount and store it as a float.
# 3. Ask the user how much tip percentage they would like to give (10%, 12%, or 15%) and store it as a float.
# 4. Ask the user for the number of people sharing the bill and store it as an integer.
# 5. Calculate the final amount each person needs to pay, including the tip.
# 6. Display the result rounded to 2 decimal places.

# Code starts here...



# Welcome message for the Tip Calculator
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to a float for calculations
bill = float(input("What was the total bill? $"))

# Ask the user for the desired tip percentage and convert it to a float for calculations
tip = float(input("How much tip would you like to give? 10, 12 or 15: % "))

# Ask how many people will split the bill and convert the input to an integer
people = int(input("How many people are splitting the bill? "))

# Calculate the total amount each person should pay by applying the tip percentage and dividing by the number of people
totalBill = (bill * (1 + tip/100))/ people # OR (bill * (tip/100) + bill)/ people

# Rounding off to 2 decimal places
finalBill = round(totalBill, 2)

# Display the final amount each person should pay
print(f"Each person should pay: ${finalBill}")