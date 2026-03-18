# num = input("Enter a number: ")  #this will consider number as string

# if num == num[::-1]:    #num[::-1] reverses the value and returns the string
#     print(f"{num} is Palindrome")
# else:
#     print(f"{num} is not Palindrome")

#using a loop

num = int(input("Enter a number: "))

orginal_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if orginal_num == reversed_num:
    print(f"{orginal_num} is Palindrome")
else:
    print(f"{orginal_num} is not Palindrome")
