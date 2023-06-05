import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


t.shape("turtle")
t.color("red")

colors = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "black", "teal", "spring green"]
directions = [0, 90, 180, 270]

t.pensize(10)
t.speed("fastest")


def random_walk():
    for _ in range(300):
        t.color(random_color())
        t.setheading(random.choice(directions))
        t.forward(random.randint(10, 30))


#random_walk()
def draw_spirograph(size):
    for n in range(int(360 / size)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size)


draw_spirograph(8)


def draw(n, color):
    t.color(color)
    for _ in range(n):
        t.right(360 / n)
        t.forward(100)


for n in range(3, 11):
    draw(n, colors[n - 3])


screen = Screen()
screen.exitonclick()
