from turtle import Screen
from player import Player
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("white")
screen.title("Pong")
screen.tracer(0)

player_one = Player(370, 0, "red")
player_two = Player(-370, 0, "blue")
ball = Ball("black")
scoreboard = Scoreboard()
speed_in_sec = 0.035
game_on = True

while game_on:
    screen.update()
    sleep(speed_in_sec)
    ball.move()

    # Collision with wall and bounce
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.wall_collision()

    # Collision with Players
    if ball.xcor() > 340 and ball.distance(player_one) < 55:
        ball.player_collision()
        speed_in_sec -= 0.001
    elif ball.xcor() < -340 and ball.distance(player_two) < 55:
        ball.player_collision()
        speed_in_sec -= 0.001

    # Player misses the ball
    if ball.xcor() > 380:
        scoreboard.increase_score_player2()
        ball.reset_position()
        player_one.reset_position(370, 0)
        player_two.reset_position(-370, 0)
        speed_in_sec = 0.035
    elif ball.xcor() < -380:
        scoreboard.increase_score_player1()
        ball.reset_position()
        speed_in_sec = 0.035
        player_one.reset_position(370, 0)
        player_two.reset_position(-370, 0)

    # Score reaches 5 points, game is off
    if scoreboard.score_player1 == 5 or scoreboard.score_player2 == 5:
        game_on = False
        sleep(5)

    screen.onkeypress(fun=player_one.go_up, key="Up")
    screen.onkeypress(fun=player_one.go_down, key="Down")
    screen.onkeypress(fun=player_two.go_up, key="w")
    screen.onkeypress(fun=player_two.go_down, key="s")
    screen.listen()
