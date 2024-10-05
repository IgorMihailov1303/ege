from turtle import *
tracer(0)
k = 30
left(90)
pendown()
begin_fill()
for _ in range(3):
    forward(7*k)
    right(90)

forward(8)

for _ in range(3):
    left(90)
    forward(5*k)

end_fill()


canvas = getcanvas()
c = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):

        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5, ):
            c += 1
print(c)

done()
