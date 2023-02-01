import random

# Randomly choose a word from the word_list and assign it to a variable called chosen_word
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
word_length = len(chosen_word)
display = ['_' for _ in range(word_length)]
print(display)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter! Which one is it? ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for num, letter in enumerate(chosen_word):
#     if letter == guess:
#         # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#         display[num] = guess

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
print(display)
