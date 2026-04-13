# 1 - Perfect Number...

n = int(input("Enter a number = "))

total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print(f"{n} is a Perfect Number...")
else:
    print(f"{n} is not a Perfect Number...")