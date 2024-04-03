from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-285,260)
        self.write(f"Level: {self.scoreboard}",align="left", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, 'center', ('Arial', 25, 'normal'))

    def score(self):
        self.scoreboard += 1
        self.update_scoreboard()

    