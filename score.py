from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.points = 0
        self.high_score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}", align="center", font=("Courier", 18, "normal"))

    def increase(self):
        self.points += 1
        self.scoreboard()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.scoreboard()



