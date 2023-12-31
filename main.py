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
state_source = pandas.read_csv("data/50_states.csv")

state_names = state_source.state.to_list()  # Create a list of states names
state_xcor = state_source.x.to_list()  # Create a list of 'X' coordinates
state_ycor = state_source.y.to_list()  # Create a list of 'Y' coordinates
state_gsd = []  # Create an empty list that will store the names of states guessed correctly
state_rem = []  # Create an empty list that will store the remaining states (NOT guessed)

st_ans_input = None
st_ans_correct = 0  # Track the number of states guessed correctly
st_ans_title = "Guess the State"  # Create a string for the title of the prompt window


# Run the game until '50' states are guessed correctly
while st_ans_correct < len(state_names):

    if st_ans_correct > 0:
        st_ans_title = f"{st_ans_correct}/50 States Correct"
    st_ans_input = screen.textinput(title=st_ans_title, prompt="Enter a state name:").title()

    # Check if the answer is inside the states names list and NOT inside the states already guessed by the user
    if st_ans_input in state_names and st_ans_input not in state_gsd:
        st_index = state_names.index(st_ans_input)
        # Write the name of the state
        writer.write_at(text=state_names[st_index],
                        location=(state_xcor[st_index], state_ycor[st_index]))
        # Add the state name to the list of 'already guessed' states
        state_gsd.append(state_names[st_index])

        st_ans_correct += 1

    elif st_ans_input == "Exit":
        for state in state_names:
            if state not in state_gsd:
                state_rem.append(state)
        state_rem_dict = {'remaining': state_rem}
        # Create a DataFrame from the dictionary of remaining states and export it to .CSV
        state_exp_df = pandas.DataFrame(state_rem_dict)
        state_exp_df.to_csv("export/state_export.csv")
        break

if st_ans_input != "Exit":
    screen.exitonclick()
