#1 - Merge list usng + operator

# list1 = list(map(int, input("Enter 1st list with space: ").split()))
# list2 = list(map(int, input("Enter 2nd list with space: ").split()))

# merged = list1 + list2

# print(f"1st List : {list1}")
# print(f"2nd List : {list2}")

# print(f"Merged list = {merged}")

# 2 - Using extend() method

list1 = list(map(int, input("Enter 1st list with space: ").split()))
list2 = list(map(int, input("Enter 2nd list with space: ").split()))

merged = list1.copy()  
list1.extend(list2)  #merged 2nd list to 1st list

print(f"1st List = {list1}")
print(f"2nd List = {list2}")
print(f"Merged list = {list1}")