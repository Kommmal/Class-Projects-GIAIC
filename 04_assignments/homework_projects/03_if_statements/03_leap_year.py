# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def main():
    year:int = int(input("Please enter a year "))
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          print("it is a leap year")
        else:
          print("it is not a leap year")
      else:
        print("it is a leap year")
    else:
      print("it is not a leap year")
if __name__ == '__main__':
    main()