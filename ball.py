from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_dir = 1
        self.y_dir = 1

    def move(self):
        time.sleep(0.1)
        self.setx(self.xcor() + self.x_dir * 10)
        self.sety(self.ycor() + self.y_dir * 10)

    def wall_bounce(self):
        self.y_dir *= -1

    def paddle_bounce(self):
        self.x_dir *= -1

    def respawn(self):
        self.goto(0, 0)
        self.x_dir *= -1
