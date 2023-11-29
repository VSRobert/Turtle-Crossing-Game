from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION) #este metoda necesara pentru a reseta jocul cand trecem de "autostrada" de masini
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y: #este valoarea setata de 280, care semnifica limita pe care trebuie sa o atingem
            return True
        else:
            return False