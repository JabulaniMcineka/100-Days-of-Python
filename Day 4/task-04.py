import random
import my_module


# ========================
# Random Numbers
# ========================
print("=== Random Numbers ===")

random_integer = random.randint(1, 20)
print(f"Random integer (1–20): {random_integer}")

random_number_0_1 = random.random() * 10
print(f"Random float (0–10): {random_number_0_1}")

random_float = random.uniform(1, 10)
print(f"Random float (1–10): {random_float}")


# ========================
# Custom Module
# ========================
print("\n=== My Module ===")

print(f"My number: {my_module.my_number}")


# ========================
# Coin Toss
# ========================
print("\n=== Coin Toss ===")

random_heads_or_tails = random.randint(0, 1)

if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")


# ========================
# Lists (Provinces)
# ========================
print("\n=== Provinces ===")

provinces = [
    "Eastern Cape",
    "Free State",
    "Gauteng",
    "KwaZulu-Natal",
    "Limpopo",
    "Mpumalanga",
    "Northern Cape",
    "North West",
    "Western Cape"
]

print(provinces)
print(f"Second province: {provinces[1]}")


# ========================
# Random Friend Picker
# ========================
print("\n=== Who Pays? ===")

friends = ["Alice", "Bob", "Charlie", "Davide", "Emanuel"]

# Option 1
print(f"Random choice: {random.choice(friends)}")

# Option 2
random_index = random.randint(0, len(friends) - 1)
print(f"Random index choice: {friends[random_index]}")