# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

def main():
   num1:int = int(input("Please enter an integer to be divided: "))
   num2:int = int(input("Please enter an integer to  divided: "))
   result: int = int(num1/num2)
   remainder: int = int(num1%num2)
   print(f"The result of this division is {result} with a remainder of {remainder}")

if __name__ == '__main__':
    main()