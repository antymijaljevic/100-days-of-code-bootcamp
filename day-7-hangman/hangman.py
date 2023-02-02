from os import system, name
import random
from art import stages, logo
from words import word_list

def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

clear_terminal()
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = ['_' for _ in range(word_length)]

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter! Which one is it? ").lower()
    
    if guess in display:
        print(f"You already tried letter '{guess}'!")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        print(f"Letter '{guess}' is not in the word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    print(f"{' '.join(display)}")
            
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])