from turtle import Turtle



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()


    def update_score(self):

        self.clear()
        self.goto(-100, 230)
        self.write(self.left_score, align="center", font=("arial", 50, "normal"))
        self.goto(-170, 230)
        self.write("A :", align="center", font=("arial", 50, "normal"))
        self.goto(100, 230)
        self.write(self.right_score, align="center", font=("arial", 50, "normal"))
        self.goto(170, 230)
        self.write(": B", align="center", font=("arial", 50, "normal"))

    def l_point(self):
        self.left_score += 1

    def r_point(self):
        self.right_score += 1