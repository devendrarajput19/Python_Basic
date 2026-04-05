# 1 - using list, map

numbers = list(map(int, input("Enter numbers separated by spaces = ").split()))

total = sum(numbers)
count = len(numbers)

average = total/count
print(f"List of number = {numbers}")
print(f"Total = {total}")
print(f"Count = {count}")
print(f"Average = {average:.2f}")

# input().split() splits the input string by spaces into a list
# map(int, ...) converts each element to integer
# sum() adds all numbers, len() counts total elements
#:.2f formats output to 2 decimal places

# 2 - using statistics module - Statistics mean directly conputes average

import statistics

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
average = statistics.mean(numbers)

print(f"List of numbers = {numbers}")
print(f"Average = {average}")