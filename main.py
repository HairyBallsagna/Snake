import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Chad Snake Game")
screen.tracer(0)

chad = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(chad.up, "w")
screen.onkey(chad.down, "s")
screen.onkey(chad.left, "a")
screen.onkey(chad.right, "d")


def reset():
    chad.reset()
    scoreboard.reset()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    chad.move()

    if chad.head.distance(food) < 15:
        food.refresh()
        chad.extend()
        scoreboard.increase_score()

    if chad.head.xcor() > 280 or chad.head.xcor() < -300 or chad.head.ycor() > 280 or chad.head.ycor() < -300:
        reset()

    for segment in chad.segments[1:]:
        if chad.head.distance(segment) < 10:
            reset()

screen.mainloop()
