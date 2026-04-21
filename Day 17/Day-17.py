class user:
    def __init__(self):
        print("new user being created....")

user_1 = user()
user_1.id= "001"
user_1.username = "angela"

print(user_1.id)
print(user_1.username)


user_2 = user()
user_2.id= "002"
user_2.username = "jack"

print(user_2.id)
print(user_2.username)

#Using a constractor to initialise variables

class User:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","angela")
user_2 = User("002","jack")

# print(user_1.followers)
# print(user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


