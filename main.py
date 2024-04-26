#
#   Classic Pong game elements:
#       Paddle, ball, score, border and centerline?
#
import time
from turtle import Screen, Turtle
from blocks import *

screen = Screen()
threshold = 10
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
border = Border(screen)
bullet = Ball()
score = Score()

left_paddle = Paddle(0)
right_paddle = Paddle(1)
screen.listen()
screen.onkeypress(left_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "Down")
screen.onkeypress(right_paddle.up, "w")
screen.onkeypress(right_paddle.down, "a")
cur_score = 0
com_score = 0


x_list = border.borders[0::2]
y_list = border.borders[1::2]
bounds = [x_list, y_list]
vector = bullet.ball_vector()
print(vector)
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.05)
    bullet.move(vector)
    for i in range(0, len(bounds)):
        for x in range(len(bounds[i])):
            if i == 0:
                if abs(int(bullet.xcor()) - bounds[i][x]) <= threshold:
                    print("End")  # s
                    game_is_on = False
                if abs(int(bullet.xcor()) - bounds[i][x]) <= threshold + 20:
                    print("loop 1")
                    print(bullet.xcor())
                    if abs(int(bullet.ycor()) - left_paddle.paddle_mid.ycor()) <= 50 and bullet.xcor() < 0:
                        vector = (vector[0] * -1, vector[1])

                        print(int(bullet.ycor()) - left_paddle.paddle_mid.ycor())
                        print("loop2")
                        cur_score += 1
                    elif abs(int(bullet.ycor()) - right_paddle.paddle_mid.ycor()) <= 50 and bullet.xcor() > 0:
                        vector = (vector[0] * -1, vector[1])
                        print(int(bullet.ycor()) - right_paddle.paddle_mid.ycor())
                        print("loop3")
                        com_score += 1
                    bullet.move(vector)
                    score.update(cur_score,com_score)


            else:
                if abs(int(bullet.ycor()) - bounds[i][x]) <= threshold:
                    vector = (vector[0], vector[1] * -1)
                    bullet.move(vector)
# TODO 1 keep paddles in bounds
# TODO 2 change score to if got by paddle instead of that breaking
# TODO 3 AI opponent
# TODO 4 Deflecting of paddle based on paddle velocity? or if it hits the edge. game is quite boring with straight on bounces currently
# TODO 5 Increase speed as score goes up

screen.exitonclick()