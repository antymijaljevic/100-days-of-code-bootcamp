from turtle import Turtle, Screen
from pandas import read_csv, DataFrame

""" setup screen """
screen = Screen()
screen.title("U.S States Game")
# screen.setup(width=700, height=500)
image = "blank_states_img.gif"
screen.addshape(image)

""" map """
turtle = Turtle()
turtle.shape(image)

""" save correct guesses """
correct_guesses = []

""" csv """
dataframe = read_csv("50_states.csv")
all_states = dataframe.state.to_list()


while len(correct_guesses) < len(all_states):
    """ asking user """
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(all_states)} States Correct", prompt="What's another state's name?").title()

    """ to exit game """
    if answer_state == "Exit":
        """ show missing states """
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        
        # print(missing_states)
        """ create a new csv with missing states """
        new_data = DataFrame(missing_states)
        new_data.to_csv("states-to-learn.csv")
        
        break

    """ put state name into belonging state area"""
    if answer_state in all_states:
        new_turtle = Turtle()
        new_turtle.hideturtle()
        turtle.penup()
        state_data = dataframe[dataframe.state == answer_state]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(state_data.state.item())
        correct_guesses.append(state_data.state.item())

screen.exitonclick()