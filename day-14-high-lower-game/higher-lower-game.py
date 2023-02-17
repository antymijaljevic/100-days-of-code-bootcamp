from game_data import data
from art import logo, vs
from os import name, system
from random import choice

def clear_terminal():
    """ 
        clears screen depends on a OS type
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
        
def format_item(item):
    """
        receives item from data and returns it formated
    """
    account_name = item['name']
    account_des  = item['description']
    account_country = item['country']
    
    return f"{account_name}, {account_des}, from {account_country}"

def compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def main():    
    """
        main
    """
    
    """ clear terminal and show logo """
    clear_terminal()
    print(logo)
    
    score = 0
    account_b = choice(data)
    
    while True:        
        """ random data """
        account_a = account_b
        while account_a == account_b:
            account_b = choice(data)
        
        """ vs section """
        print(f"Compare A: {format_item(account_a)}")
        print(vs)
        print(f"Compare B: {format_item(account_b)}")
        
        
        """ ask player and compare followers """
        player_input = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        
        """ followers """
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        
        """ compare """
        is_correct = compare(player_input, a_followers, b_followers)
        
        """ clear terminal and show logo """
        clear_terminal()
        print(logo)
        
        if is_correct:
            score += 1
            print(f"You're right. Current score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            break
            
if __name__ == "__main__":
    main()