# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def is_even(value:int):
  remainder = value % 2
  if remainder == 0:
    return True
  else:
    return False

def main():
    for i in range(10):
      print(i, end=" ")
      if is_even(i):
        print('is even')
      else:
        print('is odd')

if __name__ == '__main__':
    main()