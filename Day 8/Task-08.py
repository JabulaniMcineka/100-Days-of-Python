def greet():
    print("Hello")
    print("Hello")
    print("Hello")

greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hello {name}")
    print(f"Hello {name}")

greet_with_name("Jabulani")



def life_in_weeks(age):
    # Total weeks in a 90-year life
    total_weeks = 90 * 52

    # Weeks already lived
    weeks_lived = age * 52

    # Weeks left
    weeks_left = total_weeks - weeks_lived

    # Print result using f-string
    print(f"You have {weeks_left} weeks left.")


def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


myname = "Jabulani"
mylocation = "Durban"

# #positional Arguments
# greet_with(myname,mylocation)


#keyword Arguments
greet_with(location= mylocation,name= myname)


def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    true_total = (
        combined_names.count("t") +
        combined_names.count("r") +
        combined_names.count("u") +
        combined_names.count("e")
    )

    # Count letters in "LOVE"
    love_total = (
        combined_names.count("l") +
        combined_names.count("o") +
        combined_names.count("v") +
        combined_names.count("e")
    )

    # Combine totals to make a two-digit number
    love_score = int(f"{true_total}{love_total}")

    # Print only the number (no extra text)
    print(love_score)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Fix shift direction ONCE (not inside loop)
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
        else:
            output_text += letter  # keep spaces/symbols

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main program loop
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    if direction in ["encode", "decode"]:
        caesar(text, shift, direction)
    else:
        print("Invalid option.")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")