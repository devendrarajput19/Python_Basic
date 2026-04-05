# 1 - Using Slicing and reversing a string

string = input("Enter a Text = ")

if string == string[::-1]:
    print(f"{string} is a Palindrome...")
else:
    print(f"{string} is not a Palindrome...")

# 2 - using reversed function

string = input("Enter a Text = ")

if list(string) == list(reversed(string)):
    print(f"{string} is a Palindrome...")
else:
    print(f"{string} is not a Palindrome...")