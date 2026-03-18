num = input("Enter a number: ")  #this will consider number as string

if num == num[::-1]:    #num[::-1] reverses the value and returns the string
    print(f"{num} is Palindrome")
else:
    print(f"{num} is not Palindrome")

