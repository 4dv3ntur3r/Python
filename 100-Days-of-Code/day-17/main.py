#creating the first class

class User:
    #pass use to avoid the error when a def or class is empty
    #when the user class is called init function will run first no matter what
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user being created")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Leo")
user_2 = User("002", "Micha")

user_2.follow(user_1)

print(f"user_1 followers = {user_1.followers}")
print(f"user_1 following = {user_1.following}")
print(f"user_2 followers = {user_2.followers}")
print(f"user_2 following = {user_2.following}")