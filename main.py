import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car() #la fiecare refresh al ecranului (0.1s) vom avea o masina noua
    car_manager.move_cars()

    #Detectam coliziunea cu masinile
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  #daca distanta dintre player si oricare masina din lista all_cars este mai mica de 20 (masina are dimensiunea de 20/40), atunci oprim jocul
            game_is_on = False
            scoreboard.game_over()

    #Detectam cand playerul trece "strada" nevatamat
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()
