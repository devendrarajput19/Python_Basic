n = int(input("Enter any number: "))

a, b = 0, 1
Fib_list = []

for i in range(5):
    Fib_list.append(a)
    a, b = b, a + b

print(f"Fibonacci series = {Fib_list}")