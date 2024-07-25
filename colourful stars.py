import turtle

col = ['yellow', 'orange', 'red', 'blue', 'green', 'white', 'cyan']

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(150):
    t.color(col[i%7])
    t.forward(i*4)
    t.left(150)
    t.width(2)
