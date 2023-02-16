from game_data import data
from art import logo, vs
from os import name, system
from random import shuffle



def clear_terminal():
    """ 
        clears screen depends on a OS type
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def main():    
    """
        main
    """
    """ set score """
    score = 0
    shuffle(data)
    
    for celebrity in data:
        """ data logic """
        if celebrity['name'] == 'Instagram':
            a = f"{celebrity['name']}, {celebrity['description']}, from {celebrity['country']}."
            a_count = celebrity['follower_count']
            continue
        
        b = f"{celebrity['name']}, {celebrity['description']}, from {celebrity['country']}."
        b_count = celebrity['follower_count']
            
        """ show comparence """
        print(logo)
        print(f"Compare A: {a}")
        print(vs)
        print(f"Compare B: {b}")
        
        
        """ ask player and compare followers """
        player_input = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        clear_terminal()
        if player_input == 'a':
            if a_count > b_count:
                a = b
                a_count = b_count
                score += 1
                print(f"\nYou're right. Current score: {score}")
            else:
                print(f"\nSorry that's wrong. Final score: {score}")
                break
        else:
            if b > a:
                a = b
                a_count = b_count
                score += 1
                print(f"\nYou're right. Current score: {score}")
            else:
                print(f"\nSorry that's wrong. Final score: {score}")
                break

if __name__ == "__main__":
    main()