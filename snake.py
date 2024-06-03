from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0
class Snake:

    # tracer method is a screen method that turns off the animation whenever you needed
    # you can again turn it on by update method
   def __init__(self):
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]

   def create_snake(self):
       for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # the main thing here is understanding update method as the three segments move(for loop) then the screen is
    # updated waited for 1 sec (time.sleep(1)) then the for loop is again executed
   def move(self):
       for seg_num in range(len(self.segments) - 1, 0, -1):
        # here we are creating a situation where the last segment of snake follows segment that is in front of it
        # so when we have to turn left or right we get what we want like snake movement
           new_x = self.segments[seg_num - 1].xcor()
           new_y = self.segments[seg_num - 1].ycor()
           self.segments[seg_num].goto(new_x, new_y)
       self.head.forward(MOVE_DISTANCE)
   def update_length(self):
        length = len(self.segments)-1
        new_x = self.segments[length].xcor()
        new_y = self.segments[length].ycor()
        position = (new_x, new_y)
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

   def reset(self):
       for seg in self.segments:
             seg.goto(1000, 1000)
       self.segments.clear()
       self.create_snake()
       self.head = self.segments[0]
   def up(self):
    # if it is already going down it is not allowed to go up
       if self.head.heading() != DOWN:
            self.head.setheading(UP)
   def down(self):
       if self.head.heading() != UP:
             self.head.setheading(DOWN)
   def left(self):
       if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
   def right(self):
       if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





# the below code is written by you to create a snake body of three segments
# co_ordinates = [0,-20,-40]
# for i in range(3):
#     snake = Turtle("square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(x=co_ordinates[i] ,y=0)