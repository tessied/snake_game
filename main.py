# This is the main.py file for the snake game
# This project was inspired by the course 100 Days of Code
# Run this file to play the game

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food
    if snake.head.distance(food) < 15:
        food.change_location()
        score.increase()
        snake.extend()

    # Detect wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with self
    body = snake.snake_body[1:]
    for piece in body:
        if snake.head.distance(piece) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
