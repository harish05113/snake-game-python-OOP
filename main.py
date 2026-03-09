import random
import time
import turtle

import snake
from food import Food
from snake import Snake
from multiprocessing.resource_sharer import stop
from turtledemo.penrose import start
from scoreboard import ScoreBoard

screen = turtle.Screen()
reg = 1
print("Welcome to Snake")
High_Score = 0
while reg == 1:
    print(f"Highest score: {High_Score}")

    screen.reset()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    screen.listen()
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    border_x = [-290,290]
    border_y = [-290,290]
    score = 0

    game = True
    while game:
        turtle.write(f"Score: {score}", move="center")
        screen.update()
        time.sleep(0.1)
        snake.snake_move()
        #collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            screen.tracer(0)
            snake.grow()
            scoreboard.increase_score()
            score += 1
        if snake.game_over() == False or snake.bite()==False:
            scoreboard.game_over_board()
            game = False
            print(f"Your Score: {score}")
            if score > High_Score:
                High_Score = score
                print(f"New High Score:{High_Score}")
                print("\n"*2)
            else:
                print("\n"*2)
    repeat = screen.textinput("Play again", "press y to play again or press n to exit ")
    if repeat == "y":
        reg = 1
    else:
        reg = 0
        screen.exitonclick()