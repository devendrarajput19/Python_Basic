# 1 - Convert decimal to Binary - using bin function

decimal = int(input("Enter any number = "))
binary = bin(decimal)       

print(f"Binary = {binary}")     # Wth 0b Prefix
print(f"Binary = {binary[2:]}") # without 0b prefix

# 2 - Manual Conversion

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        remainder = n % 2               
        binary = str(remainder) + binary
        n = n//2

    return binary

decimal = int(input("Enter a decimal number: "))
print(f"Binary: {decimal_to_binary(decimal)}")