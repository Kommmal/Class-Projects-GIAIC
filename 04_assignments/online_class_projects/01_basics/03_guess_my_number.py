# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def guess():
  random_num: int = random.randint(1,99)
  guess: int = int(input("Guess My Number \nI am thinking of a number between 0 and 99... Enter a guess:  "))
  while guess != random_num:
    if guess < random_num:
      print("Your guess is too low")
    elif guess > random_num:
      print("Your guess is too high")
    guess: int = int(input("Enter a new number:  "))
  print("You guess correctly")

def main():
    guess()

if __name__ == '__main__':
    main()