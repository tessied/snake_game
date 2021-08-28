from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create an empty list where segments of the snake will be added
snake = []

for index in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.pu()
    new_turtle.color("white")
    new_turtle.goto(0 - index * 20, 0)
    snake.append(new_turtle)

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    for index in snake:
        index.forward(20)





screen.exitonclick()