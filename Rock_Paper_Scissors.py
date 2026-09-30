# 🎮 Question: Rock, Paper, Scissors Game

# Problem: Write a Python program to play Rock, Paper, Scissors with the computer.

# Rules:

# Player chooses one option: "rock", "paper", or "scissors".

# Computer randomly chooses one of these.

# Rules of winning:

# Rock beats Scissors

# Scissors beats Paper

# Paper beats Rock

# If both choices are the same → "It's a tie!"

# Game keeps running until the player types "exit".

# At the end, show total score (Player Wins vs Computer Wins)

import random

a = ["rock", "paper", "scissors"]

your_score = 0
computer_score = 0

# logic
# rock - paper
# paper - scissors
# scissors - rock

while True:
  b = random.choice(a)
  print(b)

  choose = input("rock, paper, scissors? (type exit to quit)")
  if choose == b:
    print("tie")

  elif choose == "rock":
    if b == "paper":
      print("you lose")
      computer_score += 1
      break
    elif b == "scissors":
      print("you win")
      your_score += 1

  elif choose == "paper":
    if b == "scissors":
      print("you lose")
      computer_score += 1
      break
    elif b == "rock":
      print("you win")
      your_score += 1

  elif choose == "scissors":
    if b == "rock":
      print("you lose")
      computer_score += 1
      break
    elif b == "paper":
      print("you win")
      your_score += 1

  elif choose == "exit":
    break

  else:
    print("you must choose rock, paper or scissors")
    break

print(f"your score: {your_score}", f"computer score:{computer_score}")
