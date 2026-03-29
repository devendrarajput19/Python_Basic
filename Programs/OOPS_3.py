class Car:
    @staticmethod  #Static method - for every instance/object, method is created only once. It is not created again and again.
    def start():   #They cant access class attributes.
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyataCar(Car):        #This is how we inherit any class. This is called Single inheritence
    def __init__(self, name):
        self.name = name

class Fortuner(ToyataCar):   #This is called Multiple inheritence
    def __init__(self, type):
        self.type = type

c1 = ToyataCar("Fortuner")
c2 = Fortuner("Petrol")
print(c1.name)
print(c2.type, c2.start())     # As class Car is inherited, we can access the methods and attributes.