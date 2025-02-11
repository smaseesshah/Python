# Number Guessing Game
# The computer will choose a random number between 1 and 100. The user will have to guess the number. If the user's guess is too high or too low, the computer will tell the user. If the user guesses the number correctly, the computer will congratulate the user.

import random as r

x = r.randint(1, 100)
print("Welcome to the Number Guessing Game!")
user = int(input("Choose a number between 1 and 100: "))
while user != x:
    if user > x:
        print("Too high!")
    else:
        print("Too low!")
    user = int(input("Try again: "))
print("Congratulations! You guessed the number correctly!")
