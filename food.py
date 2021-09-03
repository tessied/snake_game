# A module to generate the food particle for the snake

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.change_location()

    def change_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
