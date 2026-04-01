#Write your code below this line
print ("Hello" +" "+ " Jabulani")

#Using input function
print("Hello " + input("What is your name?") +"?")

#Using input only
input("What is your name?")

#Using variable names
name = input("What is your name?")
print(name)


#Using length fuction
name = "Jabulani"
print(len(name))

name = "Makhosonke"
print(len(name))

print(len(input("What is your name?")))

username = input("What is your name?")
length = len(username)
print(length)


#Project
# Band Name Generator

print("Welcome to the Band Name Generator! ")

city = input("What city did you grow up in? \n")
pet = input("What is the name of your pet? \n")

band_name = city + " " + pet

print("Your band name is: " + band_name + " ")