import random

# art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# players choices
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0, 2)

# data
art_values = [
    [0, rock, "Rock!"],
    [1, paper, "Paper!"],
    [2, scissors, "Scissors!"]
]

# show graphic
def result(player, comp):
    print(art_values[player][1])
    print(art_values[player][2])
    print("\nComputer choose:\n")
    print(art_values[comp][1])
    print(art_values[comp][2])

# player wins
if art_values[user_choice][0] == 0 and art_values[comp_choice][0] == 2:
    result(user_choice, comp_choice)
    print("\nYou win!")
# player wins
elif art_values[user_choice][0] == 1 and art_values[comp_choice][0] == 0:
    result(user_choice, comp_choice)
    print("\nYou win!")
# player wins
elif art_values[user_choice][0] == 2 and art_values[comp_choice][0] == 1:
    result(user_choice, comp_choice)
    print("\nYou win!")
# draw
elif user_choice == comp_choice:
    result(user_choice, comp_choice)
    print("\nDraw!")
# computer wins
else:
    result(user_choice, comp_choice)
    print("\nComputer Win!")