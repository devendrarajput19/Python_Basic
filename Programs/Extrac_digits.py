def print_digits(n):

    while n > 0:
        digit = n % 10
        print(f"Digit = {digit}")

        n = n // 10

print_digits(5941)