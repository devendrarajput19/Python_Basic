#1 - Using split function

string = input("Enter any text = ")
count = len(string.split())

print(f"Text count = {count}")

# 2 - manual counting using loop

string = input("Enter any text = ")

count = 0
for word in string.split():
    count += 1

print(f"Count = {count}")

