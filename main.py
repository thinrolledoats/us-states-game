import turtle
import pandas
from pen import Pen

writer = Pen()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)

# Create a backdrop from blank states image
blank_states_img = "data/blank_states.gif"
screen.addshape(blank_states_img)
turtle.shape(blank_states_img)

# Read the CSV file
states_source = pandas.read_csv("data/50_states.csv")

states_names = states_source.state.to_list()  # Create a list of states names
states_xcor = states_source.x.to_list()  # Create a list of 'X' coordinates
states_ycor = states_source.y.to_list()  # Create a list of 'Y' coordinates
states_guessed = []  # Create an empty list that will store the names of states guessed correctly

states_correct = 0  # Track the number of states guessed correctly
answer_state_title = "Guess the State"  # Create a string for the title of the prompt window


# Run the game until '50' states are guessed correctly
while states_correct < 50:

    if states_correct > 0:
        answer_state_title = f"{states_correct}/50 States Correct"
    answer_state = screen.textinput(title=answer_state_title, prompt="Enter a state name:").lower().title()

    # Check if the answer is inside the states names list and NOT inside the states already guessed by the user
    if answer_state in states_names and answer_state not in states_guessed:
        states_index = states_names.index(answer_state)
        # Write the name of the state
        writer.write_at(text=states_names[states_index],
                        location=(states_xcor[states_index], states_ycor[states_index]))
        # Add the state name to the list of 'already guessed' states
        states_guessed.append(states_names[states_index])

        states_correct += 1

screen.exitonclick()
