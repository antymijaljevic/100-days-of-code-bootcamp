from turtle import Turtle, Screen


"""
    Python higher-order functions are functions that take one or more functions as arguments, 
    or return a function as their result. These functions allow you to create more concise 
    and reusable code, and are a powerful feature of Python's functional programming capabilities.
"""

# def is_even(x):
#     return x % 2 == 0

# my_list = [1, 2, 3, 4, 5]
# even_list = filter(is_even, my_list)
# print(list(even_list))  # Output: [2, 4]


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)


screen.exitonclick()
