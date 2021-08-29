from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.points = 0
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.points}", align="center", font=("Courier", 18, "normal"))

    def increase(self):
        self.points += 1
        self.clear()
        self.scoreboard()

    def end_game(self):
        self.home()
        self.color("red")
        self.write("Game Over", align="center", font=("Courier", 18, "normal"))


