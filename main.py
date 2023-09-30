from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
import time

# TODO 1. setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # TODO 2. create and move the cars
    cars.create_cars()
    cars.move_cars()

    # TODO 3. Detect collision with cars
    # whenever I have to compare two thinks with each-other at that time we have to loop through it.

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # TODO 4. Detect collision with finishline

    if player.is_at_finish_line():
        player.go_start()
        cars.level_up()
        # TODO 5. Create scoreboard.
        scoreboard.increase_score()


screen.exitonclick()
