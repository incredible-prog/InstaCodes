import turtle
import colorsys
import time


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.width(5)
t.speed(0)

time.sleep(10)
n = 36
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(200)
        t.left(144)

#code by incredible_prog
