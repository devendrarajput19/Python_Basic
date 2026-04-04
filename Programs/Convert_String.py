# 1 - Using upper function

string = input("Enter any string = ")
uppercase = string.upper()

print(f"Original value = {string}")
print(f"Uppercase value = {uppercase}")

# 2 - swapcase function

string = input("Enter any text = ")

newvalue = string.swapcase()    # swap upper to lower and lower to upper

print(f"Original Text = {string}")
print(f"Updated Text = {newvalue}")

# 3 - Without built-in function

string = input("Enter a string: ")

result = ""
for char in string:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)   # ord(char) - Gets ASCII value, ord(char) - 32 = Converts lowercase to uppercase
                                     # chr(ord(char)) - converts back ASCII value to character
    else:
        result += char

print(f"Uppercase : {result}")