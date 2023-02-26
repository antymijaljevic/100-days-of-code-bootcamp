# https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
from random import choice, randint
import turtle as t

tim = Turtle()
# tim.shape("turtle")
# tim.color("black")

# # draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)



# # draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# # draw all
# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

# for num in range(3, 11):
#     tim.color(choice(colors))
#     draw_shapes(num)


# # random walk
# t.colormode(255)


# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     print(r, g, b)
#     return (r, g, b)

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# while True:
#     rand_color = random_color()
#     tim.color(rand_color)
#     tim.forward(30)
#     tim.setheading(choice(directions))
    
    
# Draw a Spirograph
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    
    return (r, g, b)

t.colormode(255)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        rand_color = random_color()
        tim.color(rand_color)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

   
draw_spirograph(5)   
    
screen = Screen()
screen.exitonclick()