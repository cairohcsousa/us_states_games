import turtle
import pandas as pd
import functions as fun

# Setup
data = pd.read_csv("50_states.csv")
states = data["state"]

screen = turtle.Screen()
screen.title("U.S. States Game")

bg_image = "blank_states_img.gif"
screen.register_shape(bg_image)
turtle.shape(bg_image)

pointer = turtle.Turtle()
pointer.speed("fastest")
pointer.hideturtle()
pointer.penup()

# Main functionalities
score = 0
answer = ""
list_of_states = list(states)  # So we can use "in" to check if the answer is in the series

while score < len(states) and (answer is not None):  # Clicking "cancel" on the input window returns None
    try:
        answer = screen.textinput(title=f"{score}/50 correct guesses", prompt="Try another state name:")
        answer = answer.title()
        if answer in list_of_states:
            score += 1
            list_of_states.remove(answer)

            answer_x_coord = int(data.loc[states == answer, "x"].item())
            answer_y_coord = int(data.loc[states == answer, "y"].item())
            fun.goto_and_draw(pointer, answer, answer_x_coord, answer_y_coord)
    except:
        continue

message = fun.end_screen(final_score=score, n_of_states_in_the_us=len(states))
screen.textinput(title="Thank you for playing.", prompt=message)

screen.mainloop()  # Closes the main window

# Writing the missing state names to a csv file
missing_states_data = pd.DataFrame(list_of_states)
missing_states_data.to_csv(path_or_buf="missing_states.csv", header=False, index=True)

