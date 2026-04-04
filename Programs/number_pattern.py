# 1 - Numbers pattern

n = int(input("Enter any number = "))

for i in range (1, n + 1):
  print("".join(str(j) for j in range(1, i + 1)))

# 2 - Pattern

n = int(input("Enter any number = "))

for i in range(1, n + 1):
  print(str(i) * i)

# 3 - Pattern

n = int(input("Enter any number = "))

for i in range(n, 0, -1):
  for j in range(1, i + 1):
    print(j, end="")
  print()


