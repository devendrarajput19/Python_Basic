#Dictionary - key value pairs - unordered, mutable/changeable & don't allow duplicate keys
# We can also store list, tuples in dictionary
# info = {
#     "name" : "Devendra",
#     "learning" : "coding"
# }
# print(info)

info = {} #empty dictionary

#set - collection of unique items. Ignores the duplicate values. set is mutable but element in set is immutable
# set = {1,2,3,4} #ths will print all the records and this can print in any order.
# set = {1,2,2,3,4} #This will print 2 only once

# collection = set() #empty set

# collection.add(1) #to add any element
# collection.remove(1) # to remove the element

# collection.add((1,2,3)) # Added tuple in set
# collection.clear() #empties the set

# set.union(set2) #combines unique value of both the set and return new set
# set.intersection(set2) #only gives comman values of both sets

#LOOP - to repeat the instruction

# count = 1
# while count <= 5 :
#     print("Learning Python")
#     count += 1

#print numbers from 1 to 100
# i = 1   
# while i <= 100 :
#     print(i)
#     i += 1

#print numbers from 100 to 1
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1

#print the multiplication table for number n
# n = int(input("Enter Number : "))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # added numbers in list
# index = 0
# while index < len(nums) :
#     print(nums[index])
#     index += 1

#program to search any number

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 49
# while i < len(nums) :
#     if(nums[i] == x) :
#         print("Found at index : ", i) 
#         break
#     else:
#         print("Finding..")
#     i += 1

#break keyword is used to break the loop
#Continue keyword terminate the current iteration and move to the next iteration. It acts as skip

#pass statement - inside the loop you skip any operations


#Write a program to fund the sum of n natural numbers
# n = 5
# sum = 0
# for i in range(n+1):  
#     sum += i

# print(sum)

#Write a program to fnd factorial
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i +=1 

print(fact)

   