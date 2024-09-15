from turtle import *
tracer(0)
k = 30
left(90)

pendown()
begin_fill()
for _ in range(12):
    right(60)
    forward(1*k)
    right(60)
    forward(1*k)
    right(270)
end_fill()

canvas = getcanvas()
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):

        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            c += 1
print(c)

done()