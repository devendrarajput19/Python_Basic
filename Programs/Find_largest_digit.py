# 1 - Largest digit in a number

number = input("Enter a number with spaces = ")

largest = max(int(digit) for digit in number if digit.isdigit())

print(f"Original list = {number}")
print(f"Largest number = {largest}")

# 2 - Check string contains digit - Using isdigit() function

string = input("Ener a string = ")

if(string.isdigit()):
    print(f"{string} contains only digits")
else:
    print(f"{string} does not contain digits")