import turtle
from random import choice

# This is used to extract colors from image using colorgram package the extracted list is named as color_list and white
# shades are removed
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 25)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113)]

timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
timmy.hideturtle()
timmy.speed(0)
timmy.penup()


timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
no_of_dots = 101


for dot_count in range(1, no_of_dots):
    timmy.dot(20, choice(color_list))

    timmy.forward(50)

    if dot_count % 10 == 0 and dot_count != 100:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen.exitonclick()
