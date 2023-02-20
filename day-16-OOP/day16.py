# import another_module
# print(another_module.another_variable)

# get module location
# python3
# import random
# print(random.__file__)
# /usr/lib/python3.10/random.py
# /home/amijaljevic/.local/lib/python3.10/site-packages/replit/__init__.py

# import turtle
# timmy = turtle.Turtle()
# print(timmy)

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)

# my_screen = Screen()
# # attribut
# print(my_screen.canvheight)

# # method
# my_screen.etableitonclick()

# # global libraries
# # https://pypi.org/

# import prettytable
# right click > go to definition
# dir(prettytable)

# https://pypi.org/project/prettytable/
from prettytable import PrettyTable

table = PrettyTable()
# print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"
print(table)

