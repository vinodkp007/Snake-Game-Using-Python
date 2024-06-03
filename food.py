import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        # we must call init method of super class
        super().__init__()
        self.shape("circle")
        self.penup()
        # normally circle is 20 by 20 pixels
        # this is to stretch the length of circle to it's half ie, 10 by 10 pixels
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)