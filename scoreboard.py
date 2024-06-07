import turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.data_text())
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        #  read the documentation to get  hold of it
        self.write(f"Score : {self.score}  High Score: {self.high_score}", align= ALIGNMENT, font= FONT)
        # the turtle is writing a string not that turtle object has become a string
    #
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER...", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
    def increase_score(self):
        self.score +=1
        self.update_score()

    def data_text(self):
        with open("data.txt") as file:
            content = file.read()
        return content