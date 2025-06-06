# -*- coding: utf-8 -*-
"""00_intro_python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TDk2ya1FIXNaeZg44jSSDU4uIwVVWu7R
"""

#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

#Prompt the user to enter the first number.

#Read the input and convert it to an integer.

#Prompt the user to enter the second number.

#Read the input and convert it to an integer.

#Calculate the sum of the two numbers.

#Print the total sum with an appropriate message.

#The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

num1 : str = input("Enter first number ")
num1 : int = int(num1)
num2 : str = input("Enter second number ")
num2 : int = int(num2)
total : int = num1 + num2
print("the total of two num is : ", total)

#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

#Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

#What's your favorite animal? cow

#My favorite animal is also cow!

question: str = input("What's your favorite animal? ")

print(f"My favorite animal is also \033[1;3m{question}\033[0m!")

# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

degrees_fahrenheit : str = input("Enter temperature in Fahrenheit: ")
degrees_fahrenheit: int = int(degrees_fahrenheit)
degrees_celsius: float = (degrees_fahrenheit - 32) * 5.0/9.0
print(f"Temperature: \033[1;3m{degrees_fahrenheit}\033[0m = {degrees_celsius}C")

# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):



Anton :int = 21

Beth :int = Anton + 6

Chen :int = Beth + 20

Drew :int = Chen + Anton

Ethan :int = Chen


print(f"Anton: {Anton}")
print(f"Beth: {Beth}")
print(f"Chen: {Chen}")
print(f"Drew: {Drew}")
print(f"Ethan: {Ethan}")

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

len1: float = float(input("What is the length of side 1? "))
len2: float = float(input("What is the length of side 2? "))
len3: float = float(input("What is the length of side 3? "))

perimeter: float = len1 + len2 + len3
print(f"The perimeter of the triangle is {perimeter}")

# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


num: float = float(input("Enter a number to see its square: "))
print(f"{num} squared is {num ** 2}")

