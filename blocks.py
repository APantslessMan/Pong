from turtle import Turtle
import random
import math


class Paddle:
    def __init__(self, player):
        self.paddle = []
        self.paddle_length = 3
        self.build_paddle(player)
        self.paddle_mid = self.paddle[1]

    def build_paddle(self, side):
        if side == 0:
            x_cor = -378
        else:
            x_cor = 370
        # build a paddle out of elements and place it on one side or the other
        for i in range(0, self.paddle_length):
            if i == 0 or i == self.paddle_length - 1:
                # make ends circle
                if i == 0:
                    segment = Turtle(shape='circle')
                    segment.goto(x_cor, 0 - i * 20 - 70)
                    segment.setheading(90)
                    segment.shapesize(stretch_len=2)
                if i == self.paddle_length - 1:
                    segment = Turtle(shape='circle')
                    segment.goto(x_cor, 0 - i * 20 + 70)
                    segment.setheading(90)
                    segment.shapesize(stretch_len=2)

            else:
                segment = Turtle(shape='square')
                segment.shapesize(stretch_len=5, stretch_wid=1)
                segment.goto(x_cor, 0 - i * 20)
                segment.setheading(90)
            segment.color('white')
            segment.up()
            segment.speed(0)
            self.paddle.append(segment)

    def move(self, direction):
        new_y = self.paddle_mid.ycor()
        if direction == 0:
            new_y += 35
        else:
            new_y -= 35
        self.paddle_mid.goto(self.paddle_mid.xcor(), new_y)
        self.paddle[0].goto(self.paddle_mid.xcor(), new_y + 45)  # Top end segment
        self.paddle[-1].goto(self.paddle_mid.xcor(), new_y - 45)

    def up(self):
        self.paddle_mid.setheading(90)
        self.move(0)

    def down(self):
        self.paddle_mid.setheading(270)
        self.move(1)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(5)
        self.bullet()

    def bullet(self):
        random_vector = random.randint(0, 360)
        # print(random_vector)
        self.setheading(random_vector)

    def move(self, vector):
        new_x = self.xcor() + vector[0] * 10
        new_y = self.ycor() + vector[1] * 10
        self.goto(new_x, new_y)

    def ball_vector(self):
        angle = self.heading()
        angle_rad = angle * (3.14159 / 180)
        bx = math.cos(angle_rad)
        by = math.sin(angle_rad)
        return bx, by

    def new_heading(self, velocity):
        if velocity[0] >= 0 and velocity[1] >= 0:  # Quadrant 1
            self.setheading(self.heading() + 90)
        elif velocity[0] < 0 <= velocity[1]:  # Quadrant 2
            self.setheading(self.heading() - 90)
        elif velocity[0] < 0 and velocity[1] < 0:  # Quadrant 3
            self.setheading(self.heading() + 90)
        elif velocity[0] >= 0 > velocity[1]:  # Quadrant 4
            self.setheading(self.heading() - 90)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.color("white")
        self.ht()
        self.speed("fastest")
        self.update(0,0)

    def update(self, cur_score, com_score):
        self.clear()
        self.write(f"Score: {cur_score} : {com_score}", align='center', font=('Terminal', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Terminal', 40, 'bold'))
class Border(Turtle):

    def __init__(self,screen):
        super().__init__()
        self.borders = []
        self.ht()
        self.speed("fastest")
        self.up()
        screen_size = [screen.window_height(), screen.window_width()]
        print(-abs(int(screen_size[0])/2))
        self.goto(-abs(int(screen_size[1])/2) + 5, screen_size[0]/2 - 30)
        self.down()
        self.color("white")
        for i in range(1, 5):
            if i % 2 == 0:
                self.forward(screen_size[0] - 45)
                self.right(90)
                self.borders.append(int(self.ycor()))
            else:
                self.forward(screen_size[1] - 17)
                self.right(90)
                self.borders.append(int(self.xcor()))
        print(self.borders)