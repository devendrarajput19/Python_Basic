class Person:
    name = "anonymous"

    # def changeName(self,name):
    #     self.name = name   #this wll create a new name attribute, but still class name is not changed

    def updateName(self,name):  
        Person.name = name   #This way I can change the name of Parent class
        self.__class__.name = name #Same as above line

    # Class methods - to access directly the class in our methods

    @classmethod
    def changeName(cls, name):
        cls.name = name    #ths is refering to class name.

p1 = Person()
p1.changeName("Devendra")
print(p1.name)
print(Person.name)