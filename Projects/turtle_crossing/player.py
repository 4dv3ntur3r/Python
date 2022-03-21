from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.player_reset()
        self.color("green")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reach_end(self):
        if self.ycor() >= 250:
            return True
        else:
            return False

    def player_reset(self):
        self.goto(STARTING_POSITION)
