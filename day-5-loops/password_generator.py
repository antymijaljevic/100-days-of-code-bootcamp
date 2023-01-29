#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy_level_password = ""
hard_level_password = ""
hard_level_list = []

for char in range(nr_letters):
    easy_level_password += random.choice(letters)
    hard_level_list.append(random.choice(letters))
    
for char in range(nr_symbols):
    easy_level_password += random.choice(symbols)
    hard_level_list.append(random.choice(symbols))

for char in range(nr_numbers):
    easy_level_password += random.choice(numbers)
    hard_level_list.append(random.choice(numbers))
    
random.shuffle(hard_level_list)
for x in hard_level_list:
    hard_level_password += x
    
print(f"Easy level password = {easy_level_password}")
print(f"Hard level password = {hard_level_password}")