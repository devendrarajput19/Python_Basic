# 1 - using GCD formula

a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

gcd = find_gcd(a, b)
lcm = (a * b) // gcd

print("First number = ", a)
print("Second number = ", b)
print("GCD number = ", gcd)
print("LCM is = ", lcm)
