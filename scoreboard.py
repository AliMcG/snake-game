from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

with open("data.txt") as file:
  high_score = int(file.read())
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = high_score
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.color("white")
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(f'{self.high_score}')
        self.current_score = 0
        self.track_score()
        
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.track_score()
        