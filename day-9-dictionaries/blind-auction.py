# replit library is broken,  so weare using python standard library
from os import system

# logo import
from art import logo

# clear screen
system("clear")

# logo
print(logo)
print("Welcome to the secret auction program.")

# bids collection
bids = {}

# main
end = True
while end:
    # user inputs
    name = input("What is your name?: ")
    bid  = int(input("What's your bid?: $"))
    
    # add to the dict
    bids[name] = bid
    
    # more entries or not
    keep_going  = input("Are there any other bidders? Press 'enter key' or type 'no'.\n")
    system("clear")
    if keep_going == "no":
        end = False

# get bider with highest offering
winner = []  
for key in bids:
    if not winner:
        winner += key, bids[key]
    elif bids[key] > winner[1]:
        winner[0], winner[1] = key, bids[key]

print(f"The winner is {winner[0].capitalize()} with a bid of ${winner[1]}")




