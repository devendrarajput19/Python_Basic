class Student:

    def __init__(self, name, marks): #self is the default parameter we pass when we create constructor
        self.name = name 
        self.marks = marks
        print("Adding new student in Database") 

s1 = Student("Devendra", 97) #Every time object is created of class, it calls the constructor
print(s1.name, s1.marks)

s2 = Student("Ravi", 88)
print(s2.name, s2.marks)  #using self parameter we can access the class objects
