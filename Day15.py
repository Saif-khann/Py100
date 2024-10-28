'''
🎲 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 15: Coffee Machine
-----------------------------------
This program simulates a coffee machine that can make espresso,
latte, and cappuccino. Users can insert coins to buy coffee, 
and the machine will check resources, process transactions, 
and make the coffee if resources are sufficient and payment 
is successful.
-----------------------------------
'''

# Menu and resources data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initialize profit and resources
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function to check if resources are sufficient for the order
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process coin input and calculate total amount
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# Function to check if the transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make coffee and deduct the required ingredients from resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Main loop to run the coffee machine
is_on = True

while is_on:
    # Prompt user for their choice
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off the machine if the user types 'off'
    if choice == "off":
        is_on = False
    # Print the report of resources if the user types 'report'
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # Process the order if the user chooses a valid drink
    else:
        drink = MENU[choice]
        # Check if resources are sufficient
        if is_resource_sufficient(drink["ingredients"]):
            # Process payment
            payment = process_coins()
            # Check if the transaction is successful
            if is_transaction_successful(payment, drink["cost"]):
                # Make the coffee
                make_coffee(choice, drink["ingredients"])
