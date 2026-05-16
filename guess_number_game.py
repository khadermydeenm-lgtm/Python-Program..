import random

# Computer thinks a random number between 1 to 100
number = random.randint(1, 100)

print(" Welcome to Guess the Number Game!")
print("Computer has chosen a number between 1 to 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print(" Too Low! Try again")

    elif guess > number:
        print("Too High! Try again")

    else:
        print(" Correct Guess!")
        print(f"You found the number in {attempts} attempts")
        break

print("Game Over")
