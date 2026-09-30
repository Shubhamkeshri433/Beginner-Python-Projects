# Write a program for a simple gussing game .

# rules:

# the computer will randomely guess number between 1 to 50.

# The player has to guess the number.

# if the guess to high, show "Too high" Try again.

# if the guess to LOW, show "Too LOW" Try again.

# keep asking until the player guess correctly.

# at the end, show the number of attempts the player took.

import random


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

guess_num = random.choice(num)
print(guess_num)

print("guess a number between 1 and 20")
guess = int(input("Enter your guess: "))

count = 0

while guess:
  count += 1

  if guess == guess_num:
    print("You guessed it right!")
    break

  elif guess > guess_num:
    print("Too high, Try again")
    guess = int(input("Enter your guess: "))

  elif guess < guess_num:
    print("Too low, Try again")
    guess = int(input("Enter your guess: "))

print(f"You Guess it in {count} tries")
