from turtle import Turtle


FONT1 = ("Courier", 15, "normal")
FONT2 = ("Courier", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear() #este necesar mereu pentru a nu se suprascrie scorul peste cel precedent
        self.write(f"Level: {self.level}", align="left", font=FONT1)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT2)