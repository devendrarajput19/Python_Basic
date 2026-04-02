# Extract digits of a number
# def print_digits(n):

#     while n > 0:
#         digit = n % 10         #give last digit of a number
#         print(f"Digit = {digit}")

#         n = n // 10       # remove last digit of a number.

# print_digits(5941)


# To return the count of the digits.

def count_digits(n):

    count = 0
    while n > 0:
        n = n // 10    # Remove the last digit
        count += 1     # count is increased by 1 if any digit is found.
    
    return count

print(count_digits(6578))