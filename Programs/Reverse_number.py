num = int(input("Enter a number: "))

orginal = num
reversed = 0

#Reverse using loop
while num != 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10

print(f"Original number is {orginal}")
print(f"Reversed number is {reversed}")