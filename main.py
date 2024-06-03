# the first lesson is all about creating a snake body of three segments you have created in a different
# way than her but to reduce the complexity after you have done urs i'm clearing and copying her code


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("My snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    # distance takes turtle object and measures the distance b/w called and argumented object
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.update_length()


#     detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        score.reset()
        snake.reset()

#     detect collision with it's own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            score.reset()
            snake.reset()
screen.exitonclick()



