import turtle as t
import random

# ---------------- SETUP ---------------- #
t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")


# ---------------- HELPER FUNCTIONS ---------------- #
def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def draw_square():
    tim.color("red")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def draw_dashed_line():
    tim.penup()
    tim.goto(-200, 0)
    tim.pendown()

    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(10)

    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))


def draw_shapes():
    colours = ["red", "blue", "green", "orange", "purple", "pink", "yellow"]

    for sides in range(3, 11):
        tim.color(random.choice(colours))
        angle = 360 / sides

        for _ in range(sides):
            tim.forward(100)
            tim.right(angle)


def fake_hero_name():
    first = ["Iron", "Dark", "Captain", "Shadow", "Mega"]
    last = ["Man", "Knight", "Blaze", "Storm", "Strike"]
    return f"{random.choice(first)} {random.choice(last)}"


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# ---------------- RUN SECTIONS ---------------- #

# 1. Square
draw_square()

# Move so drawings don’t overlap
tim.penup()
tim.goto(-200, -100)
tim.pendown()

# 2. Dashed line
draw_dashed_line()

# Move again
tim.penup()
tim.goto(0, 0)
tim.pendown()

# 3. Shapes
draw_shapes()

# 4. Random walk
random_walk()

# 5. Hero name (replacement for broken package)
print("Generated hero:", fake_hero_name())



# 6. Drawing a circle
draw_spirograph(5)


# Keep window open
screen = t.Screen()
screen.exitonclick()