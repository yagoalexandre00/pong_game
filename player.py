from turtle import Turtle
STARTING_LOCAL_POSITION = (370, 0)


class Player(Turtle):
    def __init__(self, x_cor, y_cor, color):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def reset_position(self, x_cor, y_cor):
        self.goto(x_cor, y_cor)