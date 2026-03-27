class Student:

    def __init__(self, name): #self is the default parameter we pass when we create constructor
        self.name = name #using self parameter we can access the class objects
        print("Adding new student in Database") 

s1 = Student("Devendra") #Every time object is created of class, it calls the constructor
print(s1.name)