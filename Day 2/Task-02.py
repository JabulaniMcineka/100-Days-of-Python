#subscripting
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

len("12345")

print(3*3+3/3-3)

print(3 * (3 + 3) // 3 - 3)

height = 1.65 
weight = 84

# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)


# Tip calculator
print("Welcome to tip calculator!")
# Inputs
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate tip amount
tip_amount = bill * (tip / 100)

# Total bill including tip
total_bill = bill + tip_amount

# Split per person
per_person = total_bill / people

# Round to 2 decimal places
final_amount = round(per_person, 2)

print(f"Each person should pay: ${final_amount}")