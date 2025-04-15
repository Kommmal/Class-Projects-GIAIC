
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def main():
   dice1:int = random.randint(1, 6)
   dice2:int = random.randint(1, 6)
   total:int = dice1 + dice2

   print(f"The result of dice 1 is: {dice1}")
   print(f"The result of dice 2 is: {dice2}")
   print(f"The total of both dices is: {total}")

if __name__ == '__main__':
    main()
