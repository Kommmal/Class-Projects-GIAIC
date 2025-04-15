# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    print(f"Rolled dice: {dice1} and {dice2}")

def main():
    print("Rolling two dice three times...\n")
    for i in range(3):
        print(f"Roll {i + 1}:")
        roll_dice()
        print()  # Blank line for readability

main()