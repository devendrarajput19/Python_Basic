# #String and Conditional Statements

# str1 = "This is a string.\nWe are creating it in Python." #print sentence in next line - use escape sequence characters - used to provide formatting
# print(str1)

# #contenation (merge 2 strings)
# str2 = "Devendra"
# str3 = "Rajput"
# print(str2+ " " +str3)
# len1 = len(str2)
# print(len1)

# #indexing - used to access the characters
# str = "Devendra Rajput"
# print(str[3])
# ch = str[0]
# print(ch)

# #slicing - accessing parts of string
# str = "Devendra Rajput"
# print(str[0:4])
# print(str[:5]) #for 1st index it will consider 0

# #negativeIndex - String is consider as negative index
# str = "Devendra"
# print(str[-5:-1])

# #StringFunctions
# str = "i am studying Python"
# print(str.endswith("on"))   #checks if the string ends with the given substring
# print(str.capitalize())   #capitalize the 1st letter to capital
# print(str.replace("Python", "Artifical Intelligence"))   #replace the keyword in the string
# print(str.find("y"))    #find the index of the 1st occurence
# print(str.count("from"))  #count the number of the word exists in the string

#Program to print name and get the length
# name = input("Enter your name :" )
# print("length of name is ", len(name))

#Program to find the occurence of '$' in string
# str = "Hi, $I am the $ symbol with $99.99"
# print(str.count("$"))


#Conditional Statements - if, elif, else
# light = "green"
# if(light == "red"):
#     print("Stop")
# elif(light == "green"):
#     print("GO")
# else:
#     print("LOOK")

#nested if (if inside if)

#Write a program to check number is odd or even
# num = int(input("Enter any number : "))
# rem = num % 2
# if(rem == 0):
#     print("Number is even")
# else:
#     print("Number is odd")

#Write a program to find the greatest of 3 numbers
# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))

# if(a>=b and a>=c):
#     print("First number is largest", a)
# elif(b>=c):
#     print("Second number is largest", b)
# else:
#     print("Third number is largest", c)

#Write a program to check if a number is multiple of 7
num = int(input("Enter number : "))
if(num % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")