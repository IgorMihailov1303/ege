from turtle import *
tracer(0)
k = 30
left(90)
right(45)
pendown()
begin_fill()
for _ in range(6):
    forward(5*k)
    right(45)
    forward(10*k)
    right(135)
end_fill()


canvas = getcanvas()
c = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):

        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            c += 1
print(c)

done()