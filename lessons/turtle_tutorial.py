from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
colormode(255)
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
leo.penup()
leo.goto(-250, -250)
leo.pendown()
i: int = 0
while (i < 3):
    leo.forward(500)
    leo.left(120)
    i = i + 1
bob: Turtle = Turtle()
side_length: int = 300
 
i: int = 0
while (i < 15):
    bob.forward(side_length)
    bob.left(123)
    i = i + 1
side_length = side_length * 0.97
done()
