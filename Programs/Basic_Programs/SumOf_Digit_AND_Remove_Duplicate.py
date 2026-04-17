# 1 - Sum of digits

num = int(input("Enter any number = "))

original = num
sum_digit = 0

while num > 0:
    digit = num % 10
    sum_digit += digit
    num //= 10

print(f"Number = {num}")
print(f"Sum of digits = {sum_digit}")

# 2 - using map() function

num = input("Enter any number = ")

sum_digit = sum(map(int, num))   # Convert num into int and map it and then sum it

print(f"Number = {num}")
print(f"Sum of digit = {sum_digit}")

# 3 - Using List comprehension

num = input("Enter a number = ")

sum_digit = sum([int(d) for d in num])

print(f"Number = {num}")
print(f"Sum of Digits = {sum_digit}")
