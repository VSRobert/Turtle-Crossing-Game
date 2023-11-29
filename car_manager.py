from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)  #frecventa cu care vin masinile generate este foarte mare. Astfel vom genera un numar random de la 1 la 6 si DOAR cand se va alege numarul 1 se vor crea masini. Astfel sunt sanse de 6 ori mai mici sa vina multe masini odata
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # pentru a crea un dreptunghi pe post de masina
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,
                                      250)  # Range-ul intre care vor aparea masinile, limita fiind de 300/-300, dar ne trebuie spatiu gol la inceput si sfarsit
            new_car.goto(300, random_y)  # apare in dreapta screen-ului, dar random pe axa verticala
            self.all_cars.append(new_car)  # adaugam in lista all_cars cate o masina random de fiecare data

    def move_cars(self):
        for car in self.all_cars:       #fiecare masina din lista all_cars
            car.backward(self.car_speed)   #folosim backward pentru a misca masinile in partea stanga cu cate un segment de 5 (STARTING_MOVE_DISTANCE) definit mai sus

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
