# numbers = list(map(int, input("Enter a number with spaces: ").split()))

# #input("Enter numbers separated by spaces: ")
# #.split() - Splits the string into a list of strings based on spaces - ['10', '20', '30', '40']

# #map(int, ...) - map applies a function (int) to each element - [10, 20, 30, 40]
# #list(...) - [10, 20, 30, 40]

# largest = max(numbers)   # max in-built function

# print(f"List = {numbers}")
# print(f"Largest : {largest}")

#2 - Using a Loop (Iterative):

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"List is {numbers}")
print(f"Largest : {largest}")

#3 - Using sorted() function

# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# largest = sorted(numbers)[-1]  #First sort the number in Ascending and then -1 means Last element of the list, -2 is 2nd last element
# print(f"List    : {numbers}")
# print(f"Largest : {largest}")