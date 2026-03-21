numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

#input("Enter numbers separated by spaces: "))).split() - ['10', '20', '30', '40']
#map(int()) - map data to int 10, 20, 30, 40
#list()  - to convert data to list

unique_numbers = list(set(numbers))  # Remove duplicates using set()

print(f"Original list is {numbers}")
print(f"Unique list is {unique_numbers}")