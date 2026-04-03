# 1 - Check number is positive/negative/zero
# num = float(input("Enter any number = "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# 2 - Find Square and Cube of a number

# num = float(input("Enter any number = "))

# square = num ** 2
# cube = num ** 3

# print(f"Square of a number = {square}")
# print(f"Cube of a number = {cube}")

# 3 - Print even numbers from 1 to N

# n = int(input("Enter any number = "))

# for i in range(2, n + 1, 2):
#     print(i)

#     # OR

# for i in range(2, n + 1):
#     if i % 2 == 0:
#         print(i)

# 4 - Sum of N numbers

# n = int(input("Enter any number = "))

# total = 0
# for i in range(1, n + 1):
#     total += i

# print(f"Sum of {n} = {total}")

#5 - Check if a number is Perfect number - Sum of divisors should be equal to number

n = int(input("Enter any number = "))

total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is not a Perfect Number")