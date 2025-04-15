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