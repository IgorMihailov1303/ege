from turtle import *

tracer(0)
k = 10
pendown()
begin_fill()
for i in range(6):
    forward(10*10)
    right(60)
end_fill()


canvas = getcanvas()
c = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):

        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            c += 1
print(c)

done()