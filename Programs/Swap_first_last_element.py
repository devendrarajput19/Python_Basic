# 1 - Swap first and last element

my_list = [10, 20, 30, 40]

print(f"Orginal list = {my_list}")

my_list[0], my_list[-1] = my_list[-1], my_list[0]    #my_list[0] = First element , my_list[-1] = Last element in negative index
print(f"Swap list = {my_list}")

# Python allows simultaneous swap in one line: a, b = b, a

# 2 - Print ASCII characters

print("=== Standard ASCII (0 - 127) ===")
for i in range(128):
    print(f"ASCII {i} : {chr(i)}")
