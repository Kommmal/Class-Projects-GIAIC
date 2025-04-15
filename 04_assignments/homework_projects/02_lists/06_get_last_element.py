# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last 
# element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    print("The last element is:", lst[-1])

num_elements = int(input("How many elements in the list? "))

user_list = []

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

get_last_element(user_list)

def main():
    values:list = []

    while True:
        value = input("Enter a value: ")
        if value == "":
            break  
        values.append(value)

    print("Here's the list:", values)

if __name__ == '__main__':
    main()