# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

choice = input("Do you want to code or decode? ")

if choice == "code":
  message = input("Enter your message: ")
  words = message.split()
  result = []

  for word in words:
    if len(word) < 3:
      result.append(word[::-1])
      print(*result)

      #code

    else:
      new_word = word[1:] + word[0]

      pre_suffix = ''.join(random.choices(string.ascii_letters, k=3))
      end_suffix = ''.join(random.choices(string.ascii_letters, k=3))

      result.append(pre_suffix + new_word + end_suffix)
      print(*result)

elif choice == "decode":
  message = input("Enter your message: ")
  words = message.split()
  result = []
  for word in words:
    if len(word) < 3:
      result.append(word[::-1])
      print(*result)

    else:
      stripper = word[3:-3]
      decode = stripper[-1] + stripper[:-1]
      result.append(decode)
      print(*result)
else:
  raise ValueError("Invalid choice, Choose either 'code' or 'decode'")

# print("".join(result))
