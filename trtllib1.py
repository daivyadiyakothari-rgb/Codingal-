import turtle

# Create screen
screen = turtle.Screen()
screen.setup(600, 600)

# ================= Activity 1: Square on a Canvas =================
screen.bgcolor("lightblue")
screen.title("Activity 1: Square")

pen = turtle.Turtle()
pen.color("black", "yellow")
pen.begin_fill()

for i in range(4):
    pen.forward(100)
    pen.left(90)

pen.end_fill()
pen.penup()
pen.goto(-200, 0)
pen.pendown()

# ================= Activity 2: Star =================
screen.bgcolor("black")
pen.color("white", "red")
pen.begin_fill()

for i in range(5):
    pen.forward(150)
    pen.right(144)

pen.end_fill()
pen.penup()
pen.goto(100, 0)
pen.pendown()

# ================= Activity 3: Rainbow Spiral =================
screen.bgcolor("white")
screen.title("Activity 3: Rainbow Spiral")

pen.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

size = 10
for i in range(36):
    pen.color(colors[i % 6])
    pen.forward(size)
    pen.right(60)
    size += 5

pen.hideturtle()
turtle.done()
# ================= Activity 4: Spiral Pattern =================
screen.bgcolor("white")
screen.title("Activity 4: Spiral Pattern")
pen.goto(0, 0)
pen.pendown()
pen.speed(0)
size = 5
for i in range(50):
    pen.forward(size)
    pen.right(20)
    size += 3
pen.hideturtle()
turtle.done()
