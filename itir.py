from turtle import *

color("red")
k = 20
speed(0)
hideturtle()
pendown()
seth(90)
begin_fill()
right(180)
forward(2 * k)
right(90)
forward(40 * k)
right(90)
forward(2 * k)
for i in range (4):
    seth(90)
    circle(-5 * k,180)
end_fill()
c = 0
canvas = getcanvas()
penup();
tracer(0)
for x in range(-40 * k, 20 * k, k):
    for y in range(-40 * k, 20 * k, k):
        if canvas.find_overlapping(x, y, x, y):
            c += 1
            goto(x, -y);
            dot(4, 'blue')
        else:
            goto(x, -y);
            dot(3, 'gray')

print(c)
done()