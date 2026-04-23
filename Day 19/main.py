###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as turtle_module
import random
import os

#getting a directory
print("CURRENT DIR:", os.getcwd())

rgb_colors = []
colors = colorgram.extract('Day 18/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    new_color = (r, g, b)
    rgb_colors.append(new_color)

#print(rgb_colors)



turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 101

for dots_count in range(1, number_of_dots):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()