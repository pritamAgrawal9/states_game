import turtle
import pandas as pd
STATES = 50

screen = turtle.Screen()
screen.setup(width=729,height=491)
screen.title("STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
data = pd.read_csv("50_states.csv")
guessed_state = []

while len(guessed_state) < 50:
    user_input = screen.textinput(f"Counter {len(guessed_state)} / {STATES} States Correct",
                                  prompt="What's another state name?").title()
    all_states = data["state"].to_list()

    if user_input == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States Game Sheet ")
        break


    if user_input in all_states:
        guessed_state.append(user_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_input)


