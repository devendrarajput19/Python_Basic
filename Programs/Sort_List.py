# 1 - Sort list using sort() function

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(f"Original List is {numbers}")
numbers.sort()

print(f"Sorted List is {numbers}")