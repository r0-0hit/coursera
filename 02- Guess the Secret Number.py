import random

secret_number = 6
guess = 0

while guess != secret_number :
    guess = random.randint(1, 10)
    print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)