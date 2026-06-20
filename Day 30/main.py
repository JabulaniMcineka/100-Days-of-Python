# ==========================
# 1. File & Key Exceptions
# ==========================

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}

    print(a_dictionary["non_existent_key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed.")


# ==========================
# 2. Raising Exceptions
# ==========================

height = float(input("Height (m): "))
weight = int(input("Weight (kg): "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(f"BMI: {bmi:.2f}")


# ==========================
# 3. Exercise: Fruit Pie
# ==========================

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit index out of range.")
    else:
        print(f"{fruit} pie")


make_pie(4)


# ==========================
# 4. Exercise: Facebook Likes
# ==========================

facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]


def count_likes(posts):
    total_likes = 0

    for post in posts:
        total_likes += post.get("Likes", 0)

    return total_likes


print(f"Total Likes: {count_likes(facebook_posts)}")