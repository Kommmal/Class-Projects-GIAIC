# Write a function that takes two numbers and finds the average between the two.

def find_average(num1: float, num2: float):
  avg = (num1 + num2) / 2
  return avg


def main():
    result = find_average(8, 12)
    print("The average is:", result)


if __name__ == '__main__':
    main()