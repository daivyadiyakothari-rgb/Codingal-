import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Fun with Shapes")

# Create turtle
t = turtle.Turtle()
t.speed(3)

# -------- Equilateral Triangle --------
t.penup()
t.goto(-200, 0)
t.pendown()

t.color("black", "skyblue")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# -------- Rectangle --------
t.penup()
t.goto(0, 0)
t.pendown()

t.color("black", "lightgreen")
t.begin_fill()
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# -------- Hexagon --------
t.penup()
t.goto(200, 0)
t.pendown()

t.color("black", "pink")
t.begin_fill()
for i in range(6):
    t.forward(70)
    t.left(60)
t.end_fill()

# Finish
t.hideturtle()
screen.mainloop()
