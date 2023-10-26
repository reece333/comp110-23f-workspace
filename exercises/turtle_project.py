"""A ship drifts through space."""
 
__author__ = "730564969"
 
from turtle import Turtle, done
import random

mikey: Turtle = Turtle()  # Create a Turtle object named after the coolest ninja turtle


def draw_star(x: float, y: float, size: float, color: str) -> None:
    """Draw the stars in the background."""
    mikey.penup()
    mikey.goto(x, y)
    mikey.pendown()
    mikey.color(color)
    mikey.begin_fill()
    for _ in range(5):
        mikey.forward(size)
        mikey.right(144)
    mikey.end_fill()


def draw_planet(x: float, y: float, size: float, color: str) -> None:
    """Draw a blue planet in the foreground."""
    mikey.penup()
    mikey.goto(x, y)
    mikey.pendown()
    mikey.color(color)
    mikey.begin_fill()
    mikey.circle(size)
    mikey.end_fill()


def draw_moon(x: float, y: float, size: float, color: str) -> None:
    """Draw a moon orbiting the blue planet."""
    mikey.penup()
    mikey.goto(x, y)
    mikey.pendown()
    mikey.color(color)
    mikey.begin_fill()
    mikey.circle(size)
    mikey.end_fill()


def draw_sun(x: float, y: float, size: float, color: str) -> None:
    """Draw a sun in the upper left corner."""
    mikey.penup()
    mikey.goto(x, y)
    mikey.pendown()
    mikey.color(color)
    mikey.begin_fill()
    mikey.circle(size)
    mikey.end_fill()


def draw_spaceship(x: float, y: float, size: float, color: str) -> None:
    """Draw a spaceship in the upper right corner."""
    mikey.penup()
    mikey.goto(x, y)
    mikey.setheading(90)
    mikey.pendown()
    mikey.color(color)
    mikey.begin_fill()

    for _ in range(3):
        mikey.forward(size)
        mikey.right(120)

    mikey.end_fill()


def draw_space() -> None:
    """Set the background to black and draw the full image, can adjust parameters of drawings here."""
    screen = mikey.getscreen()
    screen.bgcolor("black")

    for _ in range(100):
        x = random.uniform(-400, 400)
        y = random.uniform(-400, 400)
        size = random.uniform(5, 20)
        draw_star(x, y, size, "white")

    for _ in range(20):
        x = random.uniform(-400, 400)
        y = random.uniform(-400, 400)
        size = random.uniform(5, 20)
        draw_star(x, y, size, "yellow")

    draw_sun(-300, 300, 150, "yellow")
    draw_planet(200, -200, 100, "blue")
    draw_moon(270, -200, 30, "grey")
    draw_spaceship(300, 300, 50, "red")


if __name__ == "__main__":
    mikey.speed(0)
    mikey.hideturtle()

    draw_space()

    done()