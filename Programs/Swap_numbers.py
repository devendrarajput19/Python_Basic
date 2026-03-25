# 1 - Swap using Tuple Unpacking
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))

# print(f"Before swap: a = {a}, b = {b}")

# #swap using Tuple unpacking
# a, b = b, a
# print(f"After swap: a = {a}, b = {b}")

# 2 - Using Arithmetic operation

a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))

print(f"Before swap: a = {a}, b = {b}")

#Swap using operators
a = a + b
b = a - b
a = a - b

print(f"After Swap a = {a}, b = {b}")