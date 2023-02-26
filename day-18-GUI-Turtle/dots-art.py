# pip install colorgram.py
# https://pypi.org/project/colorgram.py/
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst_painting.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)


import turtle
from random import choice

""" hirst's colors """
color_list = [(245, 243, 240), (246, 243, 244), (206, 163, 101), (148, 68, 43), (240, 244, 241), (58, 102, 131), (169, 152, 37), (239, 240, 244), (220, 203, 136), (135, 34, 22), (208, 89, 67), (131, 165, 185), (47, 115, 78), (100, 80, 89), (240, 173, 158), (141, 183, 145), (69, 51, 45), (61, 50, 53), (13, 102, 73), (92, 143, 151), (88, 154, 113), (162, 141, 160), (17, 90, 94), (39, 58, 81), (78, 69, 46), (48, 63, 82), (83, 133, 175), (93, 48, 53), (183, 204, 169), (37, 63, 52)]


class Art:
    """ draws hirst's dot art """
    def __init__(self, colors):
        # hist colors
        self.colors = colors
        # turtle objects
        self.tim    = turtle.Turtle()
        self.screen = turtle.Screen()
        # turtle basic settings
        turtle.colormode(255)
        self.tim.speed("fastest")
        self.tim.hideturtle()
        
    def draw_dot_line(self):
        """ draws a line of 10 dots """
        for _ in range(10):
            self.tim.dot(20, choice(self.colors))
            self.tim.penup()
            self.tim.forward(50)

         
    def display_art(self):
        """ draws 10 rows of 10 dots """
        space = 50
        for _ in range(10):
            self.draw_dot_line()
            self.tim.penup()
            self.tim.goto(0, space)
            space += 50
            
        # display art
        self.screen.exitonclick() 


art = Art(color_list)
art.display_art()