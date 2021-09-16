from turtle import Screen, Turtle


class ScreenGenerator:

    def __init__(self):
        self.generate_screen()
        self.generate_line()

    def generate_screen(self):
        screen = Screen()
        screen.setup(width=1000, height=600)
        screen.bgcolor("black")
        screen.title("My Pong Game")
        screen.tracer(0)

    def generate_line(self):
        mid_line = Turtle()
        mid_line.hideturtle()
        mid_line.pencolor("white")
        mid_line.penup()
        mid_line.goto(0, 280)
        mid_line.setheading(-90)
        mid_line.width(5)

        i = 0
        is_penup = True

        while i < 38:
            i += 1
            if is_penup:
                is_penup = False
                mid_line.pendown()
            else:
                is_penup = True
                mid_line.penup()

            mid_line.forward(15)
