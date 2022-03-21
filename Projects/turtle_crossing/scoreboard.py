from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-20, 260)
        self.level = 0
        self.write("level : " + str(self.level), align="center", font=FONT)
        self.color("black")

    def score(self):
        self.level += 1
        self.clear()
        self.write("level : " + str(self.level), align="center", font=FONT)
        print(self.level)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
