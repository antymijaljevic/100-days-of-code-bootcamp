# https://docs.python.org/3/library/turtle.html
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


""" screen setup """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)   

""" snake, food and scoreboard object """
snake = Snake()
food = Food()
score_board = Scoreboard()
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
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
        
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
        
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

""" screen end """  
screen.exitonclick()

