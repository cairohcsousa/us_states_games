def goto_and_draw(turtle_object, name_to_be_written, x, y):
    turtle_object.setposition(x=x, y=y)
    turtle_object.write(arg=name_to_be_written, align='center')


def end_screen(final_score, n_of_states_in_the_us=50):
    remaining_states = n_of_states_in_the_us - final_score

    if remaining_states == 0:  # Won
        message = f"Congratulations! You have guessed all the {n_of_states_in_the_us} states in the U.S."
    elif remaining_states <= 5:
        message = f"You have come really close! You missed just {remaining_states} states."
    elif remaining_states <= 15:
        message = f"Nice one! You have missed just {remaining_states} states"
    elif remaining_states <= 25:
        message = f"Not bad! But there are still {remaining_states} for you to guess."
    else:
        message = f"Best luck next time! There are still {remaining_states} states left."

    return message