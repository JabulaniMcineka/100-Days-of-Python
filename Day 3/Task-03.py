# Day 3 Combined Exercises
# ========================

# 1. Even or Odd
print("=== Even or Odd Checker ===")
number_to_check = int(input("Enter a number: "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Rollercoaster
print("\n=== Rollercoaster Ride ===")
height_cm = int(input("What is your height in cm? "))

if height_cm >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("What is your age? "))
    
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age <= 45 and  age <= 55:
        print("Free ride")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")


# 3. BMI Calculator
print("\n=== BMI Calculator ===")

# Given values (from exercise)
weight = 85
height_m = 1.85

bmi = weight / (height_m ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")

