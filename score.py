# A module to keep track of the user's score
# Reads from and writes to a text file with the highest score

from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.points = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}",
                   align="center", font=("Courier", 18, "normal"))

    def increase(self):
        self.points += 1
        self.scoreboard()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.points = 0
        self.scoreboard()
