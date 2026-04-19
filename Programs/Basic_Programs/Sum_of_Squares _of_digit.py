# 1 - Sum of Squares usng loop

num = input("Enter a number = ")

sum_of_squares = 0

for digit in num:
    sum_of_squares += int(digit) ** 2

print(f"Number = {num}")
print(f"Digits = {' ,'.join(num)}")
print(f"Sum of Squares     : {sum_of_squares}")

# Using List comprehension

num = input("Enter a number = ")

sum_of_squares = sum([int(d) ** 2 for d in num])

print(f"Number = {num}")
print(f"Digits = {' ,'.join(num)}")
print(f"Sum of Squares     : {sum_of_squares}")
