# 1 - using GCD formula - greatest comman divisor

# a = int(input("Enter 1st number = "))
# b = int(input("Enter 2nd number = "))

# def find_gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# gcd = find_gcd(a, b)   
# lcm = (a * b) // gcd

# print("First number = ", a)
# print("Second number = ", b)
# print("GCD number = ", gcd)
# print("LCM is = ", lcm)

# 2 - Find LCM using loop

a = int(input("Enter 1st number = "))  # a = 6
b = int(input("Enter 2nd number = "))  # b = 4

greater = max(a, b)                    #this will give max number then greater = 6
lcm = greater                          #lcm = 6

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += greater                     #lcm = lcm + greater = lcm = 6 + 6, lcm = 12

print("First number = ", a)
print("Second number = ", b)
print("LCM is ", lcm)

