from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.pencolor("white")
        self.print_score()

    def print_score(self):
        self.clear()
        self.penup()
        self.goto(-50, 265)
        self.write(f"{self.score_left}", align="left", font=("Arial", 20, "normal"))
        self.penup()
        self.goto(50, 265)
        self.write(f"{self.score_right}", align="right", font=("Arial", 20, "normal"))

    def print_winner(self):
        self.home()
        self.pencolor("yellow")
        if self.score_left > self.score_right:
            self.write(f"LEFT SIDE WINS!", align="right", font=("Arial", 40, "normal"))
        elif self.score_left == self.score_right:
            self.write(f"DRAW!", align="center", font=("Arial", 40, "normal"))
        else:
            self.write(f"RIGHT SIDE WINS!", align="left", font=("Arial", 40, "normal"))
