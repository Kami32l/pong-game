from turtle import Screen
from screen import ScreenGenerator
from scoreboard import ScoreBoard
from pong_paddle import Paddle
from ball import Ball
import random
import time


def main():

    screen = Screen()
    ScreenGenerator()
    scoreboard = ScoreBoard()
    paddle_left = Paddle(-480)
    paddle_right = Paddle(480)

    screen.textinput("Are you ready?", "Click enter if you are").lower()

    def pong_game():
        ball = Ball()

        screen.listen()
        screen.onkey(paddle_left.up, "w")
        screen.onkey(paddle_left.down, "s")
        screen.onkey(paddle_right.up, "Up")
        screen.onkey(paddle_right.down, "Down")

        run = True
        start_move = True
        ball_move_up_right = False
        ball_move_down_right = False
        ball_move_down_left = False
        ball_move_up_left = False

        directions = {
            'up_right': ball.move_up_right,
            'down_right': ball.move_down_right,
            'up_left': ball.move_up_left,
            'down_left': ball.move_down_left,
        }

        direction_key = ['up_right', 'down_right', 'up_left', 'down_left']

        rand_direct = random.choice(direction_key)

        while run:
            time.sleep(0.015)

            if start_move:
                directions[rand_direct]()

            # Detect collision with wall
            if abs(ball.ycor()) > 260:
                start_move = False

                if ball.xcor() > ball.last_x and ball.ycor() > ball.last_y:
                    ball_move_up_right = False
                    ball_move_down_right = True
                    ball_move_down_left = False
                    ball_move_up_left = False

                elif ball.xcor() > ball.last_x and ball.ycor() < ball.last_y:
                    ball_move_up_right = True
                    ball_move_down_right = False
                    ball_move_down_left = False
                    ball_move_up_left = False

                elif ball.xcor() < ball.last_x and ball.ycor() > ball.last_y:
                    ball_move_up_right = False
                    ball_move_down_right = False
                    ball_move_down_left = True
                    ball_move_up_left = False

                elif ball.xcor() < ball.last_x and ball.ycor() < ball.last_y:
                    ball_move_up_right = False
                    ball_move_down_right = False
                    ball_move_down_left = False
                    ball_move_up_left = True

            if ball_move_up_right:
                ball.move_up_right()
            elif ball_move_down_right:
                ball.move_down_right()
            elif ball_move_down_left:
                ball.move_down_left()
            elif ball_move_up_left:
                ball.move_up_left()
            # else:
            #     if start_move:
            #         print("still moving from start")
            #     else:
            #         print("some direction error")

            # Detect collision with paddle
            for segment in paddle_right.segments:
                if ball.distance(segment) < 20:
                    # print("Collision with right paddle")

                    if ball.xcor() > ball.last_x and ball.ycor() > ball.last_y:
                        ball_move_up_right = False
                        ball_move_down_right = False
                        ball_move_down_left = False
                        ball_move_up_left = True

                    elif ball.xcor() > ball.last_x and ball.ycor() < ball.last_y:
                        ball_move_up_right = False
                        ball_move_down_right = False
                        ball_move_down_left = True
                        ball_move_up_left = False

            for segment in paddle_left.segments:
                if ball.distance(segment) < 20:
                    # print("Collision with left paddle")

                    if ball.xcor() < ball.last_x and ball.ycor() > ball.last_y:
                        ball_move_up_right = True
                        ball_move_down_right = False
                        ball_move_down_left = False
                        ball_move_up_left = False

                    elif ball.xcor() < ball.last_x and ball.ycor() < ball.last_y:
                        ball_move_up_right = False
                        ball_move_down_right = True
                        ball_move_down_left = False
                        ball_move_up_left = False

            # print(ball.xcor())
            if ball.xcor() >= 480:
                run = False
                scoreboard.score_left += 1
                # print("Point for left player")
                scoreboard.print_score()

            elif ball.xcor() <= -480:
                run = False
                scoreboard.score_right += 1
                # print("Point for right player")
                scoreboard.print_score()

            screen.update()

        to_continue = screen.textinput("Continue", "Do you want to play again? ").lower()

        if to_continue == "no":
            scoreboard.print_winner()
        else:
            ball.reset_ball()
            pong_game()

    pong_game()

    new_game = screen.textinput("Replay", "Do you want to play new game? ").lower()

    if new_game == "yes":
        screen.clear()
        main()

    screen.bye()


main()
