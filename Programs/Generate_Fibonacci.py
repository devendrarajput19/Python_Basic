# 1 - using recursion
# n = int(input("Enter any number: "))

# a, b = 0, 1
# Fib_list = []

# for i in range(5):
#     Fib_list.append(a)
#     a, b = b, a + b

# print(f"Fibonacci series = {Fib_list}")

# 2- using recursion

def fibonacci(n):
    if n <=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter any number = "))

fib_List = [fibonacci(i) for i in range(5)]

print(f"Fibonacci series = {fib_List}")