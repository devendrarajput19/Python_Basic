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

n = int(input("Enter any number = "))

for i in range(2, n + 1, 2):
    print(i)

    # OR

for i in range(2, n + 1):
    if i % 2 == 0:
        print(i)