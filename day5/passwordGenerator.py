import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




no_of_letters = int(input("Enter number of letters : "))
no_of_numbers = int(input("Enter number of numbers : "))
no_of_symbols = int(input("Enter number of symbols : "))

#Easy version
password = ""
for i in range(0,no_of_letters):
    password += random.choice(letters)
for i in range(0,no_of_numbers):
    password += random.choice(numbers)
for i in range(0,no_of_symbols):
    password += random.choice(symbols)

print(f"Your easy password is : {password}")

#Hard version
password = list(password)
random.shuffle(password)
hard_password = "".join(password)

print(f"A harder version of this password is : {hard_password}")
