from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.color("white")
        self.track_score()

    def track_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.track_score()