class Car:
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyataCar(Car):        #This is how we inherit any class
    def __init__(self, name):
        self.name = name

c1 = ToyataCar("Fortuner")

print(c1.name)
print(c1.start())     # As class Car is inherited, we can access the methods and attributes.