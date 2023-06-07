import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)


is_race_on = False
bet = turtle.textinput("Window Title?", "What is your bet? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_y = -150
start_x = -230

for n in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[n].penup()
    turtles[n].color(colors[n])
    turtles[n].goto(start_x, start_y)
    start_y += 50


if bet:
    is_race_on = True


while is_race_on:
    for n in range(len(turtles)):
        turtles[n].forward(random.randint(1, 10))
        if turtles[n].xcor() >= 230:
            if turtles[n].pencolor() == bet:
                print(f"You win! {turtles[n].pencolor()}")
                is_race_on = False
                break
            else:
                print(f"You lose! {turtles[n].pencolor()}")
                is_race_on = False
                break

screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()
