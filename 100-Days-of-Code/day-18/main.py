import random
import turtle

from random import choice
timmy = turtle.Turtle()
screen = turtle.Screen()

turtle_colors = ["lime green", "cyan", "crimson", "magenta", "deep pink", "dark violet", "dark blue",]
turtle.colormode(255)
#timmy.shape("turtle")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# def draw_gon(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for no_of_sides in range(3, 11):
#     timmy.color(choice(turtle_colors))
#     draw_gon(no_of_sides)

# def art_turtle():
#     timmy.pensize(15)
#     timmy.speed(0)#fastest
#     directions = [0, 90, 180, 360]
#     for _ in range(200):
#         timmy.color(choice(turtle_colors))
#         timmy.forward(30)
#         timmy.setheading(choice(directions))
#
# art_turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return ((r, g, b))
#
# timmy.pensize(15)
# timmy.speed(0)#fastest
# directions = [0, 90, 180, 360]
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(choice(directions))

timmy.speed(0)

def draw_the_circle_thingy(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(size_of_gap) # or can use timmy.setheading(timmy.heading() + size_of_gap)

draw_the_circle_thingy(5)

screen.exitonclick()
