# 1 - Multiple all elements in a list

numbers = list(map(int, input("Enter numbers with spaces = ").split()))

product = 1
for num in numbers:
    product *= num

print(f"Original numbers = {numbers}")
print(f"Multiplication of all numbers are {product}")

# 2- Using math function

import math

numbers = list(map(int, input("Enter numbers with spaces = ").split()))
product = math.prod(numbers)  # Multiply all numbers in a list

print(f"Original numbers = {numbers}")
print(f"Multiplication of all numbers are {product}")

# 3 - Find difference between max and min

numbers = list(map(int, input("Enter numbers (space separated): ").split()))

max_number = max(numbers)
min_number = min(numbers)

difference = max_number - min_number
print(f"Numbers = {numbers}")
print(f"Max number = {max_number}")
print(f"Min number = {min_number}")
print(f"Difference = {difference}")