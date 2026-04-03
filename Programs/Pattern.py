# 1- Print right-angle triangle pattern (stars)

# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     print("* " * i)

# 2 - Center aligned triangle

# n = int(input("Enter any number = "))

# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# 3 - Inverted upside down

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    print("* " * i)
