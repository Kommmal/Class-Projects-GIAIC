# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.


def count_even():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    print("Number of even numbers:", even_count)

def main():
    count_even()
if __name__ == '__main__':
    main()