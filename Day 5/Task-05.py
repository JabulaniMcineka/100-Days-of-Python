fruits = ["Apple","Peache","Pear"]
for fruit in fruits:
    print(fruit)

total=0
for number in range(1,101):
    total += number

    print(total)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)



import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

password = ""

# Make sure it has all types
password += random.choice(letters)
password += random.choice(numbers)
password += random.choice(symbols)

# Fill the rest
for i in range(9):
    password += random.choice(letters + numbers + symbols)

print("Your password is:", password)
 
    