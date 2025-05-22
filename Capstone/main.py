from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title("Welcome to Capstone Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()


	car_manager.generate_car()
	car_manager.move()
	
	#Detech collision with car
	for car in car_manager.all_cars:
		if car.distance(player) < 20:
			scoreboard.game_over()
			game_is_on = False


	#Detect successfully crossing
	if player.is_reached():
		player.go_to_start()
		car_manager.level_up()
		scoreboard.update_level()





screen.exitonclick()
