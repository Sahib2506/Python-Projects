import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#Taking user input

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Creating list
pas = []

#Generating Letters and appending it to the list
for i in range(1, nr_letters + 1):
  pas += random.choice(letters)

#Generating Symbols
for i in range(1, nr_symbols + 1):
  pas += random.choice(symbols)

#Generating Symbols
for i in range(1, nr_numbers + 1):
  pas += random.choice(numbers)

#shufffling each character inside the list
random.shuffle(pas)

#iterating through each and storing it inside variable password
password = ''
for i in pas:
  password += i

print(f"Suggested Password is {password}")


