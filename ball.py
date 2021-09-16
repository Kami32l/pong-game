from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.color("Green")
        self.speed("normal")
        self.last_x = self.xcor()
        self.last_y = self.ycor()
        self.move_up_right()

    def move_up_right(self):
        self.last_x = self.xcor()
        self.last_y = self.ycor()

        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        self.goto(new_x, new_y)

    def move_down_right(self):
        self.last_x = self.xcor()
        self.last_y = self.ycor()

        new_x = self.xcor() + 5
        new_y = self.ycor() - 5
        self.goto(new_x, new_y)

    def move_up_left(self):
        self.last_x = self.xcor()
        self.last_y = self.ycor()

        new_x = self.xcor() - 5
        new_y = self.ycor() + 5
        self.goto(new_x, new_y)

    def move_down_left(self):
        self.last_x = self.xcor()
        self.last_y = self.ycor()

        new_x = self.xcor() - 5
        new_y = self.ycor() - 5
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.hideturtle()
