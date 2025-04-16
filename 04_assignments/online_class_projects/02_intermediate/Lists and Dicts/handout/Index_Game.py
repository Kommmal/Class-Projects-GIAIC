def main():
    def access_element(lst, index):
        try:
            return lst[index]
        except IndexError:
            return "Index out of range."

    def modify_element(lst, index, new_value):
        try:
            lst[index] = new_value
            return f"Element at index {index} updated to '{new_value}'."
        except IndexError:
            return "Index out of range."

    def slice_list(lst, start, end):
        start = max(0, start)
        end = min(len(lst), end)
        return lst[start:end]

    def play_game():
        my_list = ['red', 'blue', 'green', 'yellow', 'purple']
        
        while True:
            print("\n--- List Game ---")
            print("Current list:", my_list)
            print("Choose an option:")
            print("1. Access element")
            print("2. Modify element")
            print("3. Slice list")
            print("4. Quit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                index = int(input("Enter index to access: "))
                print("Result:", access_element(my_list, index))

            elif choice == '2':
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(my_list, index, new_value))

            elif choice == '3':
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print("Sliced list:", slice_list(my_list, start, end))

            elif choice == '4':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please select from 1 to 4.")

    play_game()

if __name__ == "__main__":
    main()
