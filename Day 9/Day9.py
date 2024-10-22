'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 9: Blind Auction Project
-----------------------------------

This project implements a simple "Blind Auction" system. 
In this game, users can input their names and bid amounts. 
After all the bids are placed, the program determines the highest bidder and declares them as the winner. 
Each bidder's information is stored in a dictionary, and once the bidding is done, the highest bidder is found by comparing bid amounts.

This project uses the following:
- Functions (to handle determining the highest bid)
- Dictionaries (to store the bidders' names and bids)
- While loop (to allow multiple bids until bidding stops)
Code begins here...
-----------------------------------
'''

from art import logo

# Print the logo of the auction game (stored in an external file 'art.py')
print(logo)


# Define a function to find and print the highest bidder
def highestBidder(bidding_record):
    # Initialize variables to track the highest bid and the winner's name
    highest_bid_amount = 0
    winner = ""

    # Loop through the dictionary of bids to find the highest bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        # If the current bid is higher than the previous highest, update the highest bid and winner
        if bid_amount > highest_bid_amount:
            highest_bid_amount = bid_amount
            winner = bidder

    # Print the winner and their winning bid
    print(f"The winner is {winner} with a bid of ${highest_bid_amount}")


# Dictionary to store all bids (name as key, bid as value)
bids = {}

# Flag to control the continuation of bidding
continue_bidding = True

# Loop to allow multiple users to place bids
while continue_bidding:
    # Ask for the bidder's name
    name = input("What is your name: ")

    # Ask for the bid amount and store it as an integer
    price = int(input("Place your bid: $"))

    # Store the bid in the dictionary with the bidder's name as the key
    bids[name] = price

    # Ask if there are more bidders or if the auction should end
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    # If the user types "no", end the bidding process and declare the highest bidder
    if should_continue == "no":
        continue_bidding = False
        highestBidder(bids)
    
    # If the user types "yes", clear the screen (simulate a new round of bidding)
    elif should_continue == "yes":
        print("\n" * 100)  # This simulates clearing the screen for privacy during bids
