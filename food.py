from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        sample_x = random.randint(-280, 280)
        sample_y = random.randint(-280, 280)
        self.goto(sample_x, sample_y)
