# 1 - Sort list using sort() function

# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# print(f"Original List is {numbers}")
# numbers.sort()

# print(f"Sorted List is {numbers}")

# 2 - Using Bubble sort - Manual Algorithm

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

original = numbers.copy()
n = len(numbers)

#Bubble sort Algorithm

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"Original List is {original}")
print(f"Sorted List is {numbers}")