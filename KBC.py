# questions = [
#     "Who is the Prime Minister if India?", "What is the Capital of India?"
# ]

# options1 = ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Manmohan Singh"]

# options2 = ["Mumbai", "Kolkata", "Delhi", "Chennai"]

# labels = ["A", "B", "C", "D"]

# print(questions[0])
# for label, option in zip(labels, options1):  #internet help
#   print(f"{label} = {option}")

# # print(*options1, sep="\n")

# for i in range(1):
#   if input("Enter your answer A/B/C/D: ") == (labels[0]).strip().lower():
#     print("Correct")
#     print("You have won Rs. 1000")
#     print("Next question")
#     print(questions[1])

#     for label, option in zip(labels, options2):  #internet help
#       print(f"{label} = {option}")

#     # print(*options2, sep="\n")

#     for i in range(1):
#       if input("Enter your answer: ") == (labels[2]).strip().lower():
#         print("Correct")
#         print("You have won Rs. 10000")

#       else:
#         print("Wrong")
#         print("You have lost the game")
#         print("Game Over")
#   else:
#     print("Wrong")
#     print("You have lost the game")
#     print("Game Over")

# .
# .
# .
# .
# .
# .
# import random

# # Questions, options, and answers
# questions = [
#     "Who is the Prime Minister of India?", "What is the capital of India?",
#     "Which planet is known as the Red Planet?"
# ]

# options = [["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Manmohan Singh"],
#            ["Delhi", "Mumbai", "Kolkata", "Chennai"],
#            ["Earth", "Mars", "Jupiter", "Venus"]]

# answers = ["Narendra Modi", "Delhi", "Mars"]

# prizes = [1000, 2000, 5000]  # Prize for each correct answer
# total_amount = 0

# # Game loop
# for i in range(len(questions)):
#   print(f"\nQuestion {i+1}: {questions[i]}")

#   # Shuffle options for randomness
#   shuffled = options[i][:]
#   random.shuffle(shuffled)

#   # Labels for A, B, C, D
#   labels = ["A", "B", "C", "D"]
#   for label, option in zip(labels, shuffled):
#     print(f"{label} = {option}")

#   # User answer
#   choice = input("Your answer (A/B/C/D): ").strip().upper()

#   # Check answer
#   if choice in labels:
#     selected_option = shuffled[labels.index(choice)]
#     if selected_option == answers[i]:
#       total_amount += prizes[i]
#       print(f"Correct! You have won ₹{prizes[i]}")
#     else:
#       print("Wrong answer! Game over.")
#       break
#   else:
#     print("Invalid choice! Game over.")
#     break

# # Final prize
# print(f"\n🎉 You are taking home ₹{total_amount}")
# .
# .
# .
# .
# .
# .
# .
# .
#
questions = [
    ["What Language is use in Instagram?", "Java", "Python", "C++", "php", 2],
    ["What Language is use in Facebook?", "Java", "Python", "C++", "php", 3],
    ["What Language is use in Whatsapp?", "Java", "Python", "C++", "php", 4],
    ["What Language is use in Twitter?", "Java", "Python", "C++", "php", 1],
    ["What Language is use in Telegram?", "Java", "Python", "C++", "php", 2],
    ["What Language is use in Linkedin?", "Java", "Python", "C++", "php", 3],
    ["What Language is use in Snapchat?", "Java", "Python", "C++", "php", 4]
]

levels = [
    0,
    1000,
    10000,
    50000,
    100000,
    500000,
    1000000,
    5000000,
    10000000,
    50000000,
]
money = 0

for i in range(0, len(questions)):
  question = questions[i]
  print(f"\nQuestion for Rs,", {levels[i + 1]})
  print(questions[i][0])
  print(f" a. {question[1]}                     b. {question[2]}")
  print(f" c. {question[3]}                      d. {question[4]}")
  answer = int(input("Enter Your Answer: 1/2/3/4: 0 for quit:"))
  if answer == 0:
    money = levels[i]
    print(f"you lose in this question, final Rs. {money}")
    break
  if answer == question[-1]:
    print(f" Correct Answer, You Win Rs. {levels[i+1]}")
    if i == 1:
      money = 1000
      print("you can take money home Rs. 1000")

    elif i == 3:
      money = 50000
      print("you can take money home Rs. 50000")
    elif i == 5:
      money = 500000
      print("you can take money home Rs. 500000")
    elif i == 7:
      money = 5000000
      print("you can take money home Rs. 5000000")

  else:
    print("wrong answer")
    break

print(f"you take home is {money}")
