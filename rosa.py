import turtle

def draw_flower_and_stem(t):
    # Draw the stem
    t.color("green")
    t.pensize(5)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.setheading(90)
    t.forward(300)

    # Draw the leaves
    t.setheading(270)
    t.circle(50, 60)
    t.left(120)
    t.circle(50, 60)
    t.setheading(90)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Draw the flower (rose)
    t.color("red")
    t.pensize(2)
    for i in range(36):
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.left(130)

def write_message():
    message = turtle.Turtle()
    message.hideturtle()
    message.color("blue")
    message.penup()
    message.goto(0, -350)
    message.write("Te amo mucho mi niña hermosa", align="center", font=("Arial", 24, "bold"))

def animate_flower_and_stem():
    screen = turtle.Screen()
    screen.bgcolor("white")

    flower = turtle.Turtle()
    flower.speed(0.5)  # Cambia la velocidad aquí
    
    draw_flower_and_stem(flower)
    write_message()

    screen.mainloop()

if __name__ == "__main__":
    animate_flower_and_stem()
