# import random
# import my_module

# # random init
# random_int = random.randint(1, 100)
# print(random_int)

# # imported
# print(my_module.pi)


# # create random float
# rand_float = random.random()
# rand_float *= 10
# print(rand_float)


# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
	 
# #Write the rest of your code below this line 👇
# import random

# random_int = random.randint(0, 1)

# if random_int == 1:
#     print("Heads")
# else:
#     print("Tails")


# # lists
# fruits = ["Apple", "Banana", "Kiwi"]

# states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
#            'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
#            'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
#            'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
#            'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

# print(states[0])
# print(states[-2])
# print(states[::-1])
# states[1] = "PP"
# print(states)
# states.append("Anteland")
# print(states)
# states.extend(["EE", "UU", "EU"])
# print(states)

# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# random_index = random.randint(0, len(names)-1)
# print(f"{names[random_index]} is going to buy the meal today!")


# states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
#            'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
#            'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
#            'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
#            'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

# print(len(states))

# # list index out of range
# print((states[51]))


# fruites = ["Apples", "Pears", "Grapes"]
# vegetables = ["Spinach", "Kale", "Tomatoes"]

# dirty_dozen = [fruites, vegetables]

# print(dirty_dozen)


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# # column 2, row 3 would be entered as:
# choice_row    = int(position[-1]) -1
# choice_column = int(position[0]) -1

# map[choice_row][choice_column] = 'X'

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")