# 1 - Using string slicing

num = input("Enter a number = ")

if num == num[::-1]:    
    print(f"{num} is Palindrome...")
else:
    print(f"{num} is not Palindrome...")

# 2 - Using Loop

num = int(input("Enter any number = "))

original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original == reversed_num:
    print(f"{original} is Palindrome...")
else:
    print(f"{original} is not Palindrome...")


# Largest Element using built-in function max()

numbers = list(map(int, input("Enter list numbers with spaces = ").split()))

largest = max(numbers)
print(f"Largest number = {largest}")

# Using Loop

numbers = list(map(int, input("Enter list numbers with spaces = ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"{largest} is Largest number...")