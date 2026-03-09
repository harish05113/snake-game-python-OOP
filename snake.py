import turtle
from multiprocessing.resource_sharer import stop
from turtledemo.penrose import start
import time

import food

screen =turtle.Screen()
dis = 20
position = [(-15,0),(-30,0),(-45,0),(0,0)]
Up = 90
Down = 270
Left = 180
Right = 0

class Snake():
    def __init__(self):
        self.segment = []
        self.create_snake()
        screen= turtle.Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("My Snake Game")
        screen.tracer(0)
        screen.listen()
        self.counts = len(self.segment)-1
        self.head = self.segment[0]
        self.body = self.segment[1:self.counts]

        x = 0
        position = [(0,0),(-15,0),(-30,0),(-45,0)]
    def create_snake(self):
        for turt in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape("circle")
            new_turtle.color("green")
            new_turtle.penup()
            self.segment.append(new_turtle)
            count = len(self.segment)
            new_turtle.goto(position[turt])
            x = -15 * count

    def snake_move(self):
        for seg in range(len(self.segment)-1, 0,-1):
            new_x=self.segment[seg-1].xcor()
            new_y=self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x,new_y)
        self.head.forward(dis)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=Left:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)

    def game_over(self):
        for parts in self.body:
            x = parts.xcor()
            y = parts.ycor()
            if self.head.xcor == x and self.head.ycor == y:
                game = False
        if self.head.xcor() < -300 or self.head.xcor() > 290 or self.head.ycor() < -290 or self.head.ycor() > 300:
            print("You Lose")
            return False

    def bite(self):
        for parts in self.segment[1:]:
            if self.head.distance(parts) < 10:
                return False

    def grow(self):
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.shape("circle")
        new_turtle.color("green")
        new_turtle.speed(0)
        new_turtle.penup()
        pos = len(self.segment)-1
        self.segment.append(new_turtle)
        new_turtle.showturtle()
        self.body = self.segment[1:self.counts]





