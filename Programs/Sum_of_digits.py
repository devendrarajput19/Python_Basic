# 1 - Using Loop

# num = int(input("Enter a number: "))

# orginal = 0
# digit_sum = 0

# while num > 0:
#     digit = num % 10 #this gives you Quotient
#     digit_sum += digit
#     num //= 10   #ths removes last digit of the number

# print(f"Number = {orginal}")
# print(f"Sum of digits = {digit_sum}")

# 2 - Using sum() and map() function

# num = input("Enter a number: ")
# digit_sum = sum(map(int, num))  #map(int, num) - returns list of numbers with comma. and then it sum up the number

# print(f"Number = {num}")
# print(f"Sum is {digit_sum}")

# Using Recursion

def digit_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + digit_sum(num // 10)

num = int(input("Enter a number: "))

print(f"Number = {num}")
print(f"Sum of digits = {digit_sum(num)}")


