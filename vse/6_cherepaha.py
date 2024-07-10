from turtle import *
tracer(5)
left(90)
screensize(3000, 3000)

for x in range(2):
    forward(10*40)
    right(90)
    forward(18 * 40)
    right(90)
penup()

forward(5*40)
right(90)
forward(14*40)
left(90)

pendown()

for x in range(2):
    forward(17 * 40)
    right(90)
    forward(7 * 40)
    right(90)
penup()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*40,y*40)
        dot(5)
done()



