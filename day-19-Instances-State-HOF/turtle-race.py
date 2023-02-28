from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

class RaceTurtle:
    """ design turtle """
    def __init__(self, color, y_position):
        self.turtle = Turtle(shape="turtle")
        self.turtle.penup()
        self.x = -230
        self.y = y_position
        self.turtle.goto = self.turtle.goto(x=-230, y=y_position)
        self.turtle.color = self.turtle.color(color)
        
    def move_forward(self, distance):
        self.turtle.forward(distance)
        
    def get_x(self):
        x = self.turtle.xcor()
        return x
    
    def get_winning_color(self):
        color = self.turtle.pencolor()
        return color
        

""" create turtle objects for each color """
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
start_y = -100

for color in colors:
    turtle_instance = RaceTurtle(color, start_y)
    all_turtles.append(turtle_instance)
    start_y += 40
        

""" user input is valid """
if user_bet:
    race_on = True
   
""" run the game """ 
while race_on:
    for color_turtle in all_turtles:
        if color_turtle.get_x() > 230:
            race_on = False
            winning_color = color_turtle.get_winning_color()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            
        rand_distance = randint(0, 10)
        color_turtle.move_forward(rand_distance)
        
screen.exitonclick()