#Using Set() function

# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# #input("Enter numbers separated by spaces: "))).split() - ['10', '20', '30', '40']
# #map(int()) - map data to int 10, 20, 30, 40
# #list()  - to convert data to list

# unique_numbers = list(set(numbers))  # Remove duplicates using set()

# print(f"Original list is {numbers}")
# print(f"Unique list is {unique_numbers}")

# 2 - Using Loop

# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# unique_number = []
# for num in numbers:
#     if num not in unique_number:
#         unique_number.append(num)

# print(f"Orginal List is {numbers}")
# print(f"Unique List is {unique_number}")

# 3 - Using List Comprehension:

# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# unique_numbers = []
# [unique_numbers.append(num) for num in numbers if num not in unique_numbers]

# print(f"Original List is {numbers}")
# print(f"Unique number is {unique_numbers}")
