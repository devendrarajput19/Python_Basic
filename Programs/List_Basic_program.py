#1 - Count Even and odd numbers 

numbers = list(map(int, input("Enter numbers with spaces = ").split()))

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)

print(f"Original List = {numbers}")
print(f"Even Count = {even_count}")
print(f"Odd count = {odd_count}")

# 2 - Using Loop

numbers = list(map(int, input("Enter numbers with spaces = ").split()))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
print(f"Original List = {numbers}")
print(f"Even Count = {even_count}")
print(f"Odd count = {odd_count}")