import turtle

def draw_palestine_flag():
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("white")

    flag = turtle.Turtle()
    flag.speed(2)

    # Draw the flag background
    flag.color("#007A4D")
    flag.begin_fill()
    for _ in range(2):
        flag.forward(300)
        flag.right(90)
        flag.forward(200)
        flag.right(90)
    flag.end_fill()

    # Draw the upper white triangle
    flag.penup()
    flag.goto(-150, 100)
    flag.pendown()
    flag.color("white")
    flag.begin_fill()
    flag.right(90)
    flag.forward(100)
    flag.left(90)
    flag.forward(300)
    flag.left(90)
    flag.forward(100)
    flag.end_fill()

    # Draw the green triangle
    flag.penup()
    flag.goto(-150, 100)
    flag.pendown()
    flag.color("#007A4D")
    flag.begin_fill()
    flag.right(180)
    flag.forward(100)
    flag.right(90)
    flag.forward(150)
    flag.left(90)
    flag.forward(100)
    flag.end_fill()

    screen.mainloop()

# Call the function to draw the Palestine flag
draw_palestine_flag()
