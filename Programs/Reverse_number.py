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


#using string slicing

num = int(input("Enter a number: "))

reversed_num = int(str(num)[::-1])
print(f"Original number is {num}")
print(f"Reversed number is {reversed_num}")

#reverse using Reversed() and join()
num = input("Enter a number: ")
reversed_num = "".join(reversed(num))  #this will only work for string not integer
#It returns an iterator (a sequence you can loop through)
# reversed(num) → ['3', '2', '1']  (conceptually)
#"".join(...) = This joins all characters into a single string

print(f"Original number is {num}")
print(f"Reversed number is {reversed_num}")