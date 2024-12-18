import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle_state = turtle.Turtle()

data = pandas.read_csv("./50_states.csv")
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

correct_guess = 0
while True:
    if answer_state == "Exit":
        break
    if answer_state in data.state.to_list():
        answer_state_x = data[data.state == answer_state].x.item()
        answer_state_y = data[data.state == answer_state].y.item()
        turtle_state.goto(answer_state_x, answer_state_y)
        turtle_state.write(answer_state)
        correct_guess += 1
        if correct_guess == 50:
            break
        answer_state = screen.textinput(title=f"{correct_guess}/50 states", prompt="What's another state's name?").title()

# turtle.mainloop()
# screen.exitonclick()