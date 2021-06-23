from turtle import Turtle


class Ball(Turtle):
    def __init__(self, color):
        super(Ball, self).__init__()
        self.color(color)
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.y_move *= -1

    def player_collision(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)