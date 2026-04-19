#List - to store multiple values in list. It is build-in function. Use comma to separate

# marks = [94, 93, 92.2, 57.8]
# print(marks)
# print(marks[3])  #This get value based on indexing

#In list we can store values with different data types
#student = ["Devendra", "56.6", "Surat"]   #string are immutable (not Changeable), List are mutable (can change value)

#List Methods

# list = [2,1,3]
# list.append(4)  #adds one element at the end
# print(list)
# list.sort()  #sorts in ascending order
# list.sort(reverse=True) #sorts in descending order
# list.reverse() #reverse the list
# list.insert(index, new value)   #insert element at index
# list.remove(1) #remove the 1st occurence of element. If value 1 is twice in list, 1st value will get removed
# list.pop(index)   #remove the whole index


#Tuples in Python - Built in data type - Immutable. cannot change the value

# Tup = (2, 1, 3, 1) #round brackets are used in Tuples
# print(Tup[0])

#Tuple methods
# tup = (2, 1, 3, 1)
# tup.index(1)   #returns index of 1st occurence
# tup.count(1)   #return how many 1 are there in Tuples

#Write a program to ask user to enter names of their 3 fav movies & store them in list
# movies = []
# Movie1 = input("Enter 1st Movie")
# Movie2 = input("Enter 2nd Movie")
# Movie3 = input("Enter 3rd Movie")

# movies.append(Movie1)
# movies.append(Movie2)
# movies.append(Movie3)

# print(movies)

# movies.append(input("Enter 1st movie : "))   #another way to write
# movies.append(input("Enter 2nd movie : ")) 
# movies.append(input("Enter 3rd movie : ")) 


#WAP to check if a list contains a Palindrome of elements 

List1 = [1, 2, 3, 2, 1]   #looks same for start and end
list2 = [1, 2, 3]    #this is not a palindrome

copy_list1 = List1.copy()
copy_list1.reverse()

if(copy_list1 == List1):
    print("List is Palindrome")
else:
    print("List is not Palindrome")

