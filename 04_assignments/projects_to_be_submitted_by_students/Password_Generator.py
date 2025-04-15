import random

print("Welcome to Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"

number:int = int(input("Enter the number passwords you want: "))

length: int = int(input("Enter the length of your passwords: "))

print("Here are passwords:")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)