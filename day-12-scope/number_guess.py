# antymijaljevic@gmail.com
# Feb 14 2023

from art import logo
from os import name, system
from random import randint


def clear_terminal():
    """ 
        clears screen depends on a OS type
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    

def compare_numbers(rand, guess, try_counter):
    """
        compare guessing num and radnom and
        and print how close the guess was
    """
    if abs(guess - rand) <= 5:
        print("You're very close!!!")
    elif guess > rand:
        print("Too high!")
    elif guess < rand:
        print("Too Low!")
    elif guess == rand:
        print(f"You got it the answer was {guess}")
        return True
    
    try_counter -= 1
    return try_counter

      
def main():
    """
        main
    """  
    
    """ clear screen and logo """
    clear_terminal()
    
    """ generate random int and set level difficulty """
    random_num = randint(1, 100)
    print(f"Hidden > {random_num}")
    try_counter = 0
    
    """ ask player """
    while True:
        level = input("\nI'm thinking of a number between 1 and 100. Level 'easy' or 'hard': ")
        if level == 'easy':
            try_counter = 10
            print(f"You have {try_counter} remaining to guess the number")
            break
        elif level == 'hard':
            try_counter = 5
            print(f"You have {try_counter} remaining to guess the number")
            break
        else:
            print("Wrong input")
            
     
    while True:       
        """ player guessing """
        while True:
            try:
                guess = int(input("\nMake a guess: "))
                break
            except:
                print("Only numbers from 1 to 100!")
        
        """ compare numbers """
        compare = compare_numbers(random_num, guess, try_counter)
        
        """ results """
        if type(compare) == int:
            try_counter = compare
            print(f"You have {try_counter} remaining to guess the number")
            if try_counter == 0:
                print("\nYou've run out of guesses")
                break
        else:
            break

if __name__ == '__main__':
    main()