from turtle import Turtle
STEPS_OF_PLAYER = 10
STAR_POSITION = (0, -280)
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown", "green")
        self.penup()
        self.setheading(90)
        self.goto(STAR_POSITION)

    def go_up(self):
        self.forward(STEPS_OF_PLAYER)

    def go_start(self):
        self.goto(STAR_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False