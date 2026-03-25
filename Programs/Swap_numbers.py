# 1 - Swap using Tuple Unpacking
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f"Before swap: a = {a}, b = {b}")

#swap using Tuple unpacking
a, b = b, a
print(f"After swap: a = {a}, b = {b}")