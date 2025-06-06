# -*- coding: utf-8 -*-
"""07_information_flow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O7xkX4D5CQi5oI8H7hcWyXndKQos2j_p
"""

# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

# Here are two sample runs of the program, one for each return option (user input in bold italics):

# (Entered age is an adult age)

# How old is this person?: 35

# True

# (Entered age is not an adult age)

# How old is this person?: 7

# False



ADULT_AGE = 18

def is_adult(age):
  if age > ADULT_AGE:
    return True
  elif age < ADULT_AGE:
    return False

def main():
    age:int = int(input("How old is this person?: "))
    print(is_adult(age))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia

# Greetings Sophia!


def greet(name):
  return "Greeting "  + name + "!"

def main():
    name:str = input("What's your name? ")
    name = name.capitalize()
    print(greet(name))

if __name__ == '__main__':
    main()

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def in_range(n, low, high):
  if n >= low and n <= high:
    return True
  return False

def main():
    print(in_range(3,1,10))
    print(in_range(11,1,10))
    print(in_range(0,1,10))


if __name__ == '__main__':
    main()

# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.


def num_in_stock(fruit):
    if fruit == 'apple':
      return 2
    if fruit == 'mango':
      return 10
    if fruit == 'banana':
      return 200
    if fruit == 'orange':
      return 30
    else:
      return 0

def main():
    fruit:str = input("Enter a fruit: ")
    in_stock = num_in_stock(fruit)
    if in_stock == 0:
      print("The fruit is out of stock.")
    else:
      print("This fruit is in stock! Here is how many:", end=" ")
      print(in_stock)


if __name__ == '__main__':
    main()

# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

# You can return multiple pieces of data by separating each piece with a comma in the return line.



def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)

if __name__ == '__main__':
    main()

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function!
# If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    return num - 7

def main():
    user_input = input("Enter a number: ")
    num = int(user_input)
    result = subtract_seven(num)
    print("The result after subtracting 7 is:", result)

if __name__ == '__main__':
    main()