import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
t.width(5)
h = 0
n = 50
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += i/n
    t.color(c)
    t.forward(i*2)
    t.left(145)
