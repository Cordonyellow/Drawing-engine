import turtle
from random import randint
turtle.bgcolor("white")
t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for c in colors:
    t.color(c)
    t.forward(75)
    t.left(len(colors)*randint(5, 22))


