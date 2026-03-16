#Using Loop
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} = {factorial}")

#Using Recursion

def factorial(n):
    if n==0 and n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative number")
else:
    print(f"Factorial of {num} = {factorial(num)}")