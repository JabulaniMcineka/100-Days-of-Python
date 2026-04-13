enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope
def drink_portion():
    potion_strength = 2
    print(potion_strength)


drink_portion()
print(potion_strength)

#Global Scope
player_health = 10

def game():
    def drink_portion():
        potion_strength = 2
        print(player_health)

    drink_portion()  
print(player_health)

#Block scope(exercise)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

#Global variables using Global function
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies inside function: {enemies}")



















