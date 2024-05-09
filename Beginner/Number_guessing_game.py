# Import modules
import math
import random

# Get the lower and the upper range from user
lower = int(input("Enter a lower number: "))
upper = int(input("Enter a upper number: "))

# Generating random number between the upper and lower
x = random.randint(lower, upper)

print(f"\nyou have {round(math.log(upper - lower + 1, 2))}chances to guess the integer!")

# Initiate the number of guesses.
count = 0

# Create loop of guesses
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking guessing number from user
    guess = int(input("Enter a guess: "))

    # Condition testing
    if guess == x:
        print(f"Congratulation, You got it in {count} guesses!")
        # If correct, loop will break
        break
    if guess > x:
        print("Too high!")
    if guess < x:
        print("Too low!")

# If guessing is more than required guesses, show the output.
if count >= math.log(upper - lower + 1, 2):
    print(f'The number was {x}')
    print('Better luck next time.')
