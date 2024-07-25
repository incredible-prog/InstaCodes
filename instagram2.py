from turtle import *
speed(0)

def draw(x, y):
    penup()
    goto(x,y)
    pendown()

def draw2(x,y,f,c,c1,c2):
    color(c)
    draw(x, y)
    begin_fill()
    for i in range(4):
        forward(f)
        circle(c1,c2)
    end_fill()

def draw3(c,x,y,c1):
    color(c)
    begin_fill()
    draw(x,y)
    circle(c1)
    end_fill()

draw2(-150, -120, 350, 'pink', 20, 90)
draw2(-110, -70, 260, 'white', 20, 90)
draw2(-90, -50, 220, 'pink', 20, 90)
draw3('white', 20, 10, 70)
draw3('pink', 20, 30, 50)
draw3('white', 110, 160, 15)
hideturtle()
done()

