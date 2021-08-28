from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

for index in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(0 - index * 20, 0)


screen.exitonclick()