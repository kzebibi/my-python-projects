# Import module
import random


# Generate secret number
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicated(num):
            return num


# Split and convert the number to list
def getDigits(num):
    return [int(i) for i in str(num)]


# Check for duplications
def noDuplicated(num):
    nums = getDigits(num)
    if len(nums) == len(set(nums)):
        return True
    else:
        return False


# Get the number of bulls and cows
def NumOfBullsCows(num_, guess_):
    bull_cow_ = [0, 0]
    nums = getDigits(num_)
    guessed = getDigits(guess_)

    for i, j in zip(nums, guessed):
        if j in nums and j == i:
            bull_cow_[0] += 1
        if j in nums and j != i:
            bull_cow_[1] += 1

    return bull_cow_


if __name__ == "__main__":
    secret_num = generateNum()
    tries = 10
    print(f"Welcome to Cows and Bulls Game, Let's play!")
    print(f"You have {tries} tries!")
    try:
        while tries > 0:
            print()
            tries -= 1
            try:
                # get the guessed number from player
                guess = int(input("Enter the number (4 digits) without duplicate: "))

            except ValueError:
                print("Enter a number only!")
                continue
            # check if duplication
            if not noDuplicated(guess):
                print("Enter the number without duplicate. Try again.")
                continue
            # check if more than 4 digits or fewer
            elif guess < 1000 or guess > 9999:
                print("Enter 4 digit number only. Try again.")
                continue

            # print the numbers of bulls and cows that player guessed
            bull_cow = NumOfBullsCows(secret_num, guess)
            print(f"{bull_cow[0]} Bulls, {bull_cow[1]} Cows")

            # If the bulls = 4, then the player win
            if bull_cow[0] == 4:
                print("You guessed correct")
                print("You win!")
                break

        if tries <= 0:
            print()
            print(f"You ran out of tries. Number was {secret_num}")

    except EOFError:
        print()
        print("Bye! Try again.")
        exit()
