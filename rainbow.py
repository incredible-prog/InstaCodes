import turtle as t
import colorsys,time

t.speed(0)
t.hideturtle()
t.bgcolor('white')
t.title('Rainbow')
t.setup(700, 700)
colors = 49
radius = 300
penwidth = 20 *7/colors
hue = 0


time.sleep(10)
def draw_rainbow(x,y,r,pensize,color):
    t.up()
    t.goto(x+r,y)
    t.down()
    t.seth(90)
    t.pensize(pensize)
    t.pencolor(color)
    t.circle(r, 180)

for i in range(colors):
    (r,g,b) = colorsys.hsv_to_rgb(hue, 1, 1)

    draw_rainbow(0, -100, radius, penwidth, (r,g,b))
    radius -= penwidth-1
    hue+=0.9/colors

t.done()
