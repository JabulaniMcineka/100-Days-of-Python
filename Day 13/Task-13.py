#bug fixing

year = int(input("What's your year of birth"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")


#using try and catch
try:
    age = int(input("How old are you?"))
except ValueError:
    print("Yuo have typed in a an invalid number, Please try again with a numerical response such as 15")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")


#Problem 3
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)