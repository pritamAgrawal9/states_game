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
# print(data)

count = 0
while game_is_on:
    # count += 1
    user_input = screen.textinput(f"Counter {count} / {STATES} States Correct", prompt="What's another state name?")

    for state in data["state"]:
        if user_input.lower() == state.lower():
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == user_input]
            t.goto(int(state_data["x"]), int(state_data["y"]))
            t.write(state_data["state"])
            # count += 1
            # print(user_input)
            # game_is_on = False

screen.exitonclick()