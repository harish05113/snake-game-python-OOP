from turtle import Turtle
alignment = "center"
font = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(200, 270)
        self.pendown()
        self.write(f"SCORE: {self.score}", align=alignment, font=font)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", align=alignment, font=font)

    def game_over_board(self):
        self.goto(0,180)
        self.clear()
        self.pencolor("yellow")
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "bold"))
        self.penup()
        self.pencolor("white")
        self.goto(0, 130)
        self.pendown()
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 18, "bold"))