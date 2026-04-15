# 1 - Reverse a number

num = int(input("Enter a number = "))

original = num
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"Original number = {original}")
print(f"Reversed number = {reversed_num}")

# 2 - using string slicing

num = int(input("Enter a number: "))

reversed_num = int(str(num)[::-1])  #This is string slicing to reverse it

print(f"Original number = {num}")
print(f"Reversed number = {reversed_num}")

# 3 - using reversed() and join() function

num = input("Enter a number: ")

reversed_num = "".join(reversed(num))  #reversed(num) - It returns an iterator (a sequence you can loop through)

print(f"Original number = {num}")
print(f"Reversed number = {reversed_num}")

#reversed(num) → ['3', '2', '1']  (conceptually)
#"".join(...) = This joins all characters into a single string


