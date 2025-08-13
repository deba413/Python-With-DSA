import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Durga Thakur")

# Create a turtle
t = turtle.Turtle()

# Function to draw a circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(color, width, height, x, y):
    t.penup()
    t.goto(x - width / 2, y - height / 2)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Draw the face
draw_circle("brown", 50, 0, 0)

# Draw the eyes
draw_circle("white", 10, -20, 20)
draw_circle("white", 10, 20, 20)

# Draw the pupils
draw_circle("black", 5, -20, 25)
draw_circle("black", 5, 20, 25)

# Draw the mouth
t.penup()
t.goto(-20, 10)
t.pendown()
t.right(90)
t.circle(20, 180)

# Draw the crown
draw_rectangle("red", 80, 20, 0, 50)
draw_rectangle("red", 60, 20, 0, 70)
draw_rectangle("red", 40, 20, 0, 90)

# Hide the turtle and display the drawing
t.hideturtle()
screen.mainloop()