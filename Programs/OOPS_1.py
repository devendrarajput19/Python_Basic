# class Student:

#     def __init__(self, name, marks): #self is the default parameter we pass when we create constructor
#         self.name = name 
#         self.marks = marks
#         print("Adding new student in Database") 

# s1 = Student("Devendra", 97) #Every time object is created of class, it calls the constructor
# print(s1.name, s1.marks)

# s2 = Student("Ravi", 88)
# print(s2.name, s2.marks)  #using self parameter we can access the class objects

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is", sum/3)

s1 = Student("Devendra", [92, 55, 66])
s1.get_avg()    


