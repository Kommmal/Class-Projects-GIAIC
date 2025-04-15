# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers: list) -> int:
  total = 0
  for num in numbers:
    total += num
  return total

def main():
    list_of_numbers: list = [1,2,3,4,5]
    total_sum: int = sum_of_numbers(list_of_numbers)
    print(total_sum)

if __name__ == '__main__':
    main()