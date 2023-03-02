# https://docs.python.org/3/library/turtle.html
from turtle import Screen
from time import sleep
from snake import Snake


""" screen setup """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)   

""" snake object """
snake = Snake()
game_is_on = True

""" listener """
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


""" main play """
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    


""" screen end """  
screen.exitonclick()

