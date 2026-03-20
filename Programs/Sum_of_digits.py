num = int(input("Enter a number: "))

orginal = 0
digit_sum = 0

while num > 0:
    digit = num % 10 #this gives you Quotient
    digit_sum += digit
    num //= 10   #ths removes last digit of the number

print(f"Number = {orginal}")
print(f"Sum of digits = {digit_sum}")

