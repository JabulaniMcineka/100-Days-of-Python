import random
import hangman_words
import hangman_stages


lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(f"Pssst, the word is: {chosen_word}")  # for testing

# Placeholder
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed '{guess}'")
        continue

    display = ""

    # Build display
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Wrong guess
    if guess not in chosen_word:
       lives -= 1
       print(f"You guessed {guess}, that's not in the word. Lives left: {lives}")

    if lives == 0:
        print("**********************You lose.***********************")
        game_over = True
        break

    # Win condition
    if "_" not in display:
        game_over = True
        print("**********************You win!*********************")

    # Show stage
    print(hangman_stages.stages[lives])