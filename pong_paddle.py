from turtle import Screen, Turtle
screen = Screen()

class Paddle:
    def __init__(self, position):
        self.position = position
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        starting_positions = [(self.position, 20), (self.position, 40), (self.position, 60)]
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        screen.update()

    def move(self):
        screen.update()

    def up(self):
        for segment in self.segments:
            y_cor = segment.ycor()
            if y_cor < 240:
                y_cor += 60
            segment.setpos(self.position, y_cor)
            self.move()

    def down(self):
        for segment in self.segments:
            y_cor = segment.ycor()
            if y_cor > -240:
                y_cor -= 60
            segment.setpos(self.position, y_cor)
            self.move()
