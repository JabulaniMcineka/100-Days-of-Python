#Final Project
from random import randint #for random numbers.

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function the check the users guess against actual answer.
#Track the number of turns and reduce by 1 if they get it wrong.
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns  thye number of turns remaining."""
    if  user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


#Function to set the difficulty level.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



#=========================main function==================================================


def game():
    #choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number betwwen 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, The correct answer is {answer}")




    turns = set_difficulty()
    
    guess =0
    #Repeat the guessing functionality if they get it wrong. 
    while guess != answer:
        print(f"You have {turns} atttemps remaining to guess the number.")
        #let the user guess nunmber number.
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
        
game()




        