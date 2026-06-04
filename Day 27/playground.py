# def add(number):
#     sum = 0
#     while number > 0:
#         sum += number
#         number -= 1
#     return sum



# input_number = int(input("Enter a number: "))
# result = add(input_number)
# print(f"The sum of numbers from 1 to {input_number} is: {result}")

#unlimited arguments
def add(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum



add(1,2,34,4,5)