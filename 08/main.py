from os import system, name
from art import logo

def clearScreen():

    # for windows
    if name == "nt":
        system("cls")
    #linux and macOS
    else:
        system("clear")

# Adds a bidder and their amount to the dictionary
def add_bid(name, amount):
    bids[name] = amount

# Sweet ASCII art
print(logo)
print("Welcome to the secret auction")

more_bidders = True
bids = {}

# Main aution part of the program. Runs until there are no more bidders
while more_bidders:
    bid_name = input("What is your name: ")
    bid_amount = int(input("Whats your bid? $"))
    add_bid(bid_name, bid_amount)

    another_one = input("Are there any other bidders? Y/N: ").lower()

    clearScreen()
    if another_one == "n":
        more_bidders = False

# Determine who had the highest bid
max_bid = 0
winner = ""
for bidder_name in bids:
    if bids[bidder_name] > max_bid:
        winner = bidder_name
        max_bid = bids[bidder_name]

print(f"The winner is {winner.capitalize()} with a bid of ${max_bid}.")
    
