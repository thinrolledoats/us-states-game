import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)

blank_states_img = "data/blank_states.gif"
screen.addshape(blank_states_img)
turtle.shape(blank_states_img)

states_src = pandas.read_csv("data/50_states.csv")
states_names = states_src['state'].to_list()
states_xcor = states_src['x'].to_list()
states_ycor = states_src['y'].to_list()

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess a state", prompt="Enter a state name:").lower().title()
    if answer_state in states_names:
        states_index = states_names.index(answer_state)
        print(states_index)

screen.exitonclick()
