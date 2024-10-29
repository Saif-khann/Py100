'''
🎲 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 16: Coffee Machine OOP
-----------------------------------
This program uses object-oriented programming (OOP) principles 
to simulate a coffee machine with a menu of drinks (espresso, 
latte, cappuccino). The program manages resources, processes 
payments, and delivers coffee if requirements are met. Users 
can select drinks, view machine reports, and turn the machine off.
-----------------------------------
'''

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize components for the coffee machine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Machine control loop
is_on = True

while is_on:
    # Get available menu options
    options = menu.get_items()
    # Prompt user for their choice
    choice = input(f"What would you like? ({options}): ")
    
    # Turn off the machine if 'off' is selected
    if choice == "off":
        is_on = False
    # Print resource and profit reports if 'report' is selected
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the chosen drink from the menu
        drink = menu.find_drink(choice)
        
        # Check if resources and payment are sufficient to make the coffee
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)