import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25/day-25-us-states-game-start/blank_states_img.gif"    
screen.addshape(image)
turtle = turtle.Turtle()


pandas = pandas.read_csv("Day 25/day-25-us-states-game-start/50_states.csv")
all_states = pandas["state"].to_list() 
guessed_states = []    


while len(guessed_states) < 50:  
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)


    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = pandas[pandas.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        print("Correct!")


screen.exitonclick()