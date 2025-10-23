import random
import string

print("Welcome to password generator project!")

letters_list = list(string.ascii_letters)
numbers_list = list(string.digits)
symbols = ['@', ')', '(', '#', '$']

letters = int(input("How many letters do you need?: "))
numbers = int(input("How many numbers do you need?: "))
symbol = int(input("How many symbols do you need?: "))

password = []

for i in range(letters):
    password.append(random.choice(letters_list))

for i in range(numbers):
    password.append(random.choice(numbers_list))

for i in range(symbol):
    password.append(random.choice(symbols))

random.shuffle(password)
final_password = "".join(password)

print("Your generated password is:", final_password)
