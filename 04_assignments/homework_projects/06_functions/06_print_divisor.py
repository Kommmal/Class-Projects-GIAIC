# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12



def print_divisors(num):
  for i in range(1,num):
    current_num = i+1
    if num % current_num == 0:
      print(current_num)


def main():
    user_input: int = int(input("Enter the number you wanna double: "))
    num = user_input
    print_divisors(num)


if __name__ == '__main__':
    main()