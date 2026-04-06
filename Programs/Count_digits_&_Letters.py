# 1- Count digits and letters

string = input("Enter any string = ")

digit = sum(1 for char in string if char.isdigit())
letters = sum(1 for char in string if char.isalpha())

print(f"Original String = {string}")
print(f"Digit count = {digit}")
print(f"Character count = {letters}")

# 2 - Using loop

string = input("Enter any string = ")

digit = 0
letters = 0

for char in string:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letters += 1

print(f"Original String = {string}")
print(f"Digit count = {digit}")
print(f"Letter count = {letters}")