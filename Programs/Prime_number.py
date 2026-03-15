#num = int(input("Enter a number: "))

# if num <= 1:
#     print(f"{num} is not a Prime")
# else:
#     is_Prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_Prime:
#         print(f"{num} is Prime")
#     else:
#         print(f"{num} is not Prime")

# Program using Function

def is_Prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
num = int(input("Enter a number: "))
if is_Prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is not Prime")