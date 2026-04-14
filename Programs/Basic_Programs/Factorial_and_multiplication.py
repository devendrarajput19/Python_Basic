# 1 - Multiplication of a number

num = int(input("Enter any number"))

for i in range(1, 11):
    print(f"{num} * {i:2} = {num * i}")


# 2 - Calculate Factorial - Using Loop

num = int(input("Enter any number = "))

if num < 0:
    print("Factorial si not defined for negative numbers")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    print(f"Factorial of {num} = {factorial}")

# 3 - Factorial - Using Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter any number = "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial of {num} = {factorial(num)}")


