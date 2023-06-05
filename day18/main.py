import turtle
from turtle import Turtle, Screen
from cgram import color_list
import random

t = Turtle()
t.hideturtle()
t.penup()
turtle.colormode(255)
start_x = -220
start_y = -220

for _ in range(10):
    t.sety(start_y)
    for _ in range(10):
        t.setx(start_x)
        t.dot(20, random.choice(color_list))
        start_x += 50
    start_x = -220
    start_y += 50


# 50 10 * 10



screen = Screen()
screen.exitonclick()
