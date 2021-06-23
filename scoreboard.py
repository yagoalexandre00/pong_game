from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier New', 30, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.penup()
        self.hideturtle()
        self.goto(-20, 250)
        self.color("black")
        self.write(f"{self.score_player2} \t {self.score_player1}", align=ALIGNMENT, font=FONT)

    def increase_score_player1(self):
        self.score_player1 += 1
        self.clear()
        self.write(f"{self.score_player2} \t {self.score_player1}", align=ALIGNMENT, font=FONT)

    def increase_score_player2(self):
        self.score_player2 += 1
        self.clear()
        self.write(f"{self.score_player2} \t {self.score_player1}", align=ALIGNMENT, font=FONT)


    # def pause(self):
    #     self.goto(-20, 0)
    #     for second in range(30):
    #         sleep(1)
    #         self.write(f"PAUSE {(second-30)*-1}", align=ALIGNMENT, font=FONT)
    #         self.clear()
