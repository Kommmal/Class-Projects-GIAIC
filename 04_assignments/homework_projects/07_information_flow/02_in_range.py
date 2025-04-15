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