from turtle import Turtle
MOVE_STEPS = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create()
        self.head = self.snake_body[0]

    def create(self):
        for index in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.pu()
            new_turtle.color("white")
            new_turtle.goto(0 - index * 20, 0)
            self.snake_body.append(new_turtle)

    def move(self):
        for index in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[index].goto(self.snake_body[index - 1].pos())
        self.head.forward(MOVE_STEPS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading != 180:
            self.head.setheading(0)



