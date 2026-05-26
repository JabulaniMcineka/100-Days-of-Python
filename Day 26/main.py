# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n ** 2 for n in numbers]
# print(squared_numbers)




# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']

# numbers = [int(n) for n in list_of_strings]
# result = [n for n in numbers if n % 2 == 0]

# print(result)


# with open("file1.txt") as file1:
#     list1 = [int(num) for num in file1.readlines()]

# with open("file2.txt") as file2:
#     list2 = [int(num) for num in file2.readlines()]

# result = [num for num in list1 if num in list2]

# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = len(sentence)
print(result)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)



weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}

print(weather_f)