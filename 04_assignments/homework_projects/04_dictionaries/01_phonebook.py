# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def main():
    phonebook = {}

    while True:
        action = input("Do you want to add or look up a contact? (add/lookup/quit): ").strip().lower()

        if action == "add":
            name = input("Enter the contact's name: ").strip()
            number = input("Enter their phone number: ").strip()
            phonebook[name] = number
            print(f"Added {name} to the phonebook.")

        elif action == "lookup":
            name = input("Enter the name to look up: ").strip()
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print(f"{name} is not in the phonebook.")

        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type add, lookup, or quit.")

if __name__ == '__main__':
    main()
