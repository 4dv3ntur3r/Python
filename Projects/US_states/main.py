import turtle
import pandas


def get_mouse_click_coor(x, y):
    """To get the coordinates of the mouse click """
    print(x, y)


# To run the function to get the mouse coordinates
# turtle.onscreenclick(get_mouse_click_coor)

with open("./score.txt", mode="r") as score:
    score = score.read()

screen = turtle.Screen()
screen.title("US State Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_file = pandas.read_csv("./50_states.csv")

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.speed(0)
style = ("Arial", 8, "normal")

states_data = data_file.state.to_list()
correct_guesses = []
with open("./correct_guesses.txt", mode="r") as correct_guess_txt:
    get_inp = correct_guess_txt.read().split(",")
    for i in get_inp:
        if i != '':
            correct_guesses.append(i)

if len(correct_guesses) != 0:
    for item in correct_guesses:
        location = data_file[data_file["state"] == item]
        text.goto(float(location["x"]), float(location["y"]))
        text.write(item, move=True, font=style, align='center')
        # print(correct_guesses)

while score != len(states_data):
    guess = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state?").title()

    if guess == "Exit":
        with open('./correct_guesses.txt', 'w') as correct_file:
            states = ""
            for state in correct_guesses:
                states += state + ","
            correct_file.write(states)
        break
    if guess in states_data:
        if guess not in correct_guesses:
            location_x = float(data_file[data_file["state"] == guess]["x"])
            location_y = float(data_file[data_file["state"] == guess]["y"])
            text.goto(location_x, location_y)
            text.write(guess, move=True, font=style, align='center')

            correct_guesses.append(guess)
            score = int(score)
            score += 1
            with open("./score.txt", 'w') as file:
                file.write(str(score))

# To keep screen on replacement fot exitonclick
# turtle.mainloop()
