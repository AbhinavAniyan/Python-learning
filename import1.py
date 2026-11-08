# import random

# randint
# choice

# print(random.randint(1, 100))  # prints a random integer between 1 and 10

# fruit=("apple", "banana", "cherry", "kiwi")
# print(random.choice(fruit))  # prints a random fruit from the tuple


# coin = ("heads", "tails")
# print(random.choice(coin))  # prints a random coin side from the tuple


# z=random.randint(0,1)
# print("heads")if z else print("tails")
# if z:
#     print("heads")
# else:
#     print("tails")


# rock paper scissors game
# import random
# choices = ["rock", "paper", "scissors"]
# user = input('choose rock, paper or scissors: ')
# computer = random.choice(choices)
# if user == computer:
#     print("tie")
# elif (user == "rock" and computer == "scissors"):
#     if (user == "paper" and computer == "rock"):
#         print("user wins")
#     else:
#         print("computer wins")


# import random

# choices = ["left", "right", "straight"]

# user = input("Choose left, right or straight: ")
# computer = random.choice(choices)

# print("Computer chose:", computer)

# if user == computer:
#     print("You are racing together!")
# elif user == "left" and computer == "right":
#     print("User wins")
# else:
#     print("Computer wins")