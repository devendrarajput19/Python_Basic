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

