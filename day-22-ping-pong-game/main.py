"""
1 create the screen *
2 create and move a paddle *
3 create another paddle
4 create the ball and make it move
5 detect collision with wall and bounce
6 detect when paddle misses
7 keep score

paddle wid 20, height 100, x_pos 350 y_pos 0
"""
from turtle import Screen, Turtle

""" screen setup """
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

""" paddle setup """
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

""" paddle moves """
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)        

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y) 


""" main play """
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
""" exit game with mouse click """  
screen.exitonclick()