from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", move=False, font=("Courier", 80, "normal",))
        self.goto(100, 200)
        self.write(self.r_score, align="center", move=False, font=("Courier", 80, "normal",))
        pass

    def update_left_score(self):
        self.l_score += 1
        self.update_score()
        pass

    def update_right_score(self):
        self.r_score += 1
        self.update_score()
        pass
