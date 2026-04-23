from turtle import Turtle, Screen
import random

# def move_forward():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading) 

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()



# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(move_forward, "d")
# clear()


tim = Turtle()
screen= Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -100
step = 30  # controls spacing

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle .penup()
    new_turtle .color(colours[turtle_index])
    new_turtle .goto(x, y)
    y += step 
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in  all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You have won! The {winning_colour}  turtle is the winner!")
            else:
                print(f"You have lost! The {winning_colour}  turtle is the winner!")
                
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
