from turtle import *

tracer(0)
pendown()
speed(50000)

k = 25

for i in range(4):
    forward(8*k)
    right(90)

for i in range(3):
    forward(12*k)
    right(120)

for x in range(0,15):
    for y in range(-15,1):
        penup()
        setpos(x*k,y*k)
        dot(3)
        pendown()

done()
