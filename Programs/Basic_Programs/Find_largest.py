# 1 - Find largest number 

num1 = float(input("Enter 1st number = "))
num2 = float(input("Enter 2nd number = "))
num3 = float(input("Enter 3rd number = "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is largest number...")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is largest number...")
else:
    print(f"{num3} is largest number...")

# 2 - Using max function

largest = max(num1, num2, num3)
print(f"The largest number = {largest}")

# 3 - Factorial of a number

num = int(input("Enter any number = "))

factorial = 1
if num < 0:
    print(f"Factorial cannot be defined for negative numbers...")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} ={factorial}")