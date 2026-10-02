import random

upper_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["$", "#", "@", "!", "&", "+", "-", "_", "="]
generation = []
choise_list = [upper_abc, abc, numbers, symbols]
password = ""

num_sym_in_password = int(input("How many symbols would you like?: "))

for i in range(num_sym_in_password):
    generation.append(random.choice(choise_list))

for i in generation:
    if i == upper_abc:
        password += str(random.choice(upper_abc))
    elif i == abc:
        password += str(random.choice(abc))
    elif i == numbers:
        password += str(random.choice(numbers))
    elif i == symbols:
            password += str(random.choice(symbols))

print(f"Your generated password: {password}")