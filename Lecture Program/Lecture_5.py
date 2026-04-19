#Functions - Block of statement that perform a specific task
# def func_name(param1, param2, ....) - Function Definition
#func_name(arg1, arg2, ....) - calling a function

#Write a program to find n number factorial 

# def cal_factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_factorial(5)

#WAP to convert USD to INR

# def converter(usdValue):
#     inrValue = usdValue * 83
#     print(usdValue, "USD = ", inrValue, "INR")

# converter(10) 

#WAP if a number is ODD print ODD and print EVEN if number is EVEN

# def validate(n):
#     if(n%2 == 0):
#         print("Even")
#     else:
#         print("ODD")

# validate(10)


#Recursion - function calls itself. It is similar to loop, this work is done by function
#we have to provide condition in recursion which will stop the loop
def show(n):
    if(n == 0):   #base case
        return   
    print(n)
    show(n-1)

show(5)