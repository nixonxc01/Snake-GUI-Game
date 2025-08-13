from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('White')
        self.penup()
        self.hideturtle()
        self.goto(x=-0, y=260)
        self.write(f'Score: {self.score}',False, align="center",font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False, align="center", font=('Arial', 24, 'normal'))

    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game over! Final Score: {self.score}', False, align="center", font=('Arial', 24, 'normal'))


