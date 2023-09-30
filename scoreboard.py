from turtle import Turtle
SCORE = 1


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(-300, 250)
        self.hideturtle()
        self.score = SCORE
        self.write(f"Score: 0", align='center', font=("Courier", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Courier", 24, "normal"))
        self.score += SCORE

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align='center', font=("Courier", 24, "normal"))
