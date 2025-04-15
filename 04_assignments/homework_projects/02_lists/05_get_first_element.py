# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    print("The first element is:", lst[0])

num_elements = int(input("How many elements in the list? "))

user_list = []

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

get_first_element(user_list)