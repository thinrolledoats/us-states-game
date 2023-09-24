from turtle import Turtle
FONT = ('Fixedsys', 8, 'normal')


class Pen(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor(59/255, 59/255, 51/255)
        self.penup()

    def write_at(self, text, location):
        self.goto(location)
        self.pendown()
        self.write(arg=text, align='center', font=FONT)
        self.penup()
