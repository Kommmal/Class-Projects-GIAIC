# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:



def main():
    curr_value:int = int(input("Enter a number you wanna double: "))
    while curr_value < 100:
      curr_value = curr_value * 2
      print(curr_value, end=" ")


if __name__ == '__main__':
    main()