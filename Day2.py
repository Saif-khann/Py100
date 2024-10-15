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