def print_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)

    even_list = []  # empty list to collect even numbers

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_list.append(num)

    if even_list:
        print(f"Even numbers between {start} and {end}")
        print(even_list)

a = int(input("Enter first number  (a): "))
b = int(input("Enter second number (b): "))
print_even_numbers(a, b)